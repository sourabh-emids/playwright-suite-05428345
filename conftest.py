"""Shared fixtures: base_url wiring and one-time authenticated session reuse.

Do not hand-edit tests/features/ or tests/steps/ -- regenerate the suite
instead. This file, utils/, and pages/base_page.py are yours to customize.
"""
import json
import os
import re
from pathlib import Path

import pytest

from utils.config import BASE_URL, TEST_USERNAME, TEST_PASSWORD, has_credentials

_AUTH_STATE_PATH = Path(__file__).parent / ".auth" / "state.json"

# Read by the Automation Architect's Runner while this suite is still
# executing inside a sandbox container, one line at a time, to show pass/
# fail counts climbing live in Run History instead of jumping once at the
# end -- a container's own exit code and pytest's JUnit XML (written whole,
# only at process exit) can't provide that on their own. Purely additive:
# nothing here changes what `make test` or CI produce, it only adds one more
# file under the already-gitignored reports/ directory.
_LIVE_RESULTS_PATH = Path(__file__).parent / "reports" / "live_results.ndjson"
_EMITTED_NODEIDS: set[str] = set()
_PENDING_REPORTS: dict[str, dict[str, pytest.TestReport]] = {}
_skip_live_reporting = False


def _example_label(nodeid: str) -> str | None:
    """A Scenario Outline's Examples rows all glue to the same
    tests/test_<issue_id>_<name>.py file, so the Runner's file-based nodeid
    -> TestCase mapping necessarily collapses every example's result onto
    one shared tc_id -- correct, but it makes Run History show the same
    tc_id several times with nothing to tell the rows apart. Pytest's own
    parametrize id is already sitting right there in the nodeid as a
    trailing "[...]" (e.g. "[Solutions-Solutions-Solutions]", the Examples
    row's own column values hyphen-joined) -- this pulls just that part out
    so the frontend can render it alongside tc_id. None for a
    non-parametrized scenario, where there's only ever one row per tc_id and
    nothing to disambiguate.
    """
    match = re.search(r"\[(.+)\]$", nodeid)
    return match.group(1) if match else None


def _short_reason(report: pytest.TestReport) -> str | None:
    """The one-line summary Run History shows for a failed/errored test --
    not the full pytest traceback (fixture-call frames, source context,
    Playwright's own resolved-locator dump), just the exception's own
    headline message. `reprcrash.message` is the same short crash message
    `_is_code_defect` already keys off of; only its first line is kept here,
    since Playwright's own AssertionError message can itself run to several
    lines (a strict-mode violation's resolved-elements list, its call log)
    that add noise without adding value in a one-line row. Falls back to
    `str(longrepr)`'s first line when there's no reprcrash at all (a plain
    string longrepr a hookwrapper set) rather than showing nothing.
    """
    if report.longrepr is None:
        return None
    crash = getattr(report.longrepr, "reprcrash", None)
    message = crash.message if crash is not None else str(report.longrepr)
    first_line = message.strip().splitlines()[0] if message.strip() else None
    return first_line or None


def _is_code_defect(report: pytest.TestReport) -> bool:
    """True when a `call`-phase failure's actual exception is not the
    controlled `AssertionError` Playwright's own `expect(...).to_have_X()`
    raises for a genuine value mismatch -- e.g. a raw
    `playwright._impl._errors.Error` (a strict-mode violation: a locator
    matched more than one element, a call on a closed page, an invalid
    selector) or a plain Python `TypeError`/`AttributeError` from a bad API
    call. Confirmed against a real failure, not assumed: a locator matching
    two elements raises Playwright's own `Error`, distinct from the
    `AssertionError` a value-mismatch assertion raises -- the former is a
    defect in the generated suite's own locator/code, the latter is the
    test doing exactly its job. `reprcrash` is only present for a report
    with a real Python-exception traceback, never for the plain string
    longrepr a hookwrapper could otherwise set.
    """
    crash = getattr(report.longrepr, "reprcrash", None)
    message = getattr(crash, "message", "") if crash is not None else ""
    return not message.lstrip().startswith("AssertionError")


def pytest_configure(config: pytest.Config) -> None:
    """Distinguishes the xdist controller from the process that actually ran
    a test -- under `-n auto`, pytest-xdist replays every worker's report a
    second time in the controller for terminal-style plugins, and without
    this guard the NDJSON emitter below would write each result twice.
    `workerinput` only exists on a worker's own config; `option.dist` is
    xdist's own flag for "distribution is active at all" -- both are the
    same building blocks xdist uses internally, not a private API.
    """
    global _skip_live_reporting
    is_worker = hasattr(config, "workerinput")
    is_distributing = getattr(config.option, "dist", "no") != "no"
    _skip_live_reporting = is_distributing and not is_worker


def pytest_runtest_logreport(report: pytest.TestReport) -> None:
    """Appends one JSON line per finished test, flushed and fsynced
    immediately so a host process polling this file mid-run sees it as soon
    as it lands.

    Deliberately emitted at `teardown`, never at `call` -- confirmed by
    hitting the alternative, not just theorized: pytest-playwright's own
    trace/screenshot/video-on-failure capture happens inside a fixture's
    *teardown* finalizer, which pytest always runs strictly after `call`'s
    report has already fired. A host process polling this file the moment
    a `call` failure line landed would go looking for evidence that doesn't
    exist on disk yet. `teardown` always fires for every test regardless of
    outcome (pytest tears down whatever fixtures did get set up even after
    a setup or call failure), so waiting for it costs nothing and is the
    only phase where "the test is completely finished, artifacts included"
    is actually true.

    Each test's setup/call reports are buffered in `_PENDING_REPORTS` until
    that guaranteed final teardown report arrives, then combined into one
    status: a setup failure/skip means the test never reached `call` at all
    (`error`/`skipped` respectively -- a setup failure is a defect in the
    generated suite itself, not the same signal as a genuine assertion
    failure); a `call` failure is further split by `_is_code_defect` into
    `failed` (a genuine `AssertionError` -- the test ran and asserted
    something false) or `error` (anything else -- a raw Playwright API
    error or a Python exception escaping the generated step/page-object
    code, a defect in the suite, not a verdict about the app). A rare
    teardown-only failure after an already-good setup+call is not allowed to
    downgrade that result -- a cleanup crash after the test itself already
    passed or failed is a separate concern, not this test's own verdict.
    """
    if _skip_live_reporting:
        return

    if report.when != "teardown":
        _PENDING_REPORTS.setdefault(report.nodeid, {})[report.when] = report
        return

    if report.nodeid in _EMITTED_NODEIDS:
        return
    _EMITTED_NODEIDS.add(report.nodeid)

    phases = _PENDING_REPORTS.pop(report.nodeid, {})
    setup = phases.get("setup")
    call = phases.get("call")
    if setup is not None and setup.outcome in ("failed", "skipped"):
        status = "error" if setup.outcome == "failed" else "skipped"
        source = setup
    elif call is not None:
        status = "error" if call.outcome == "failed" and _is_code_defect(call) else call.outcome
        source = call
    else:
        # Neither a usable setup nor call report reached teardown -- should
        # not normally happen, but "error" is the safe default: never
        # silently drop a test's result.
        status = "error"
        source = report

    _LIVE_RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    line = json.dumps(
        {
            "nodeid": report.nodeid,
            "file": report.nodeid.split("::")[0],
            "when": source.when,
            "status": status,
            "duration": source.duration,
            "longrepr": _short_reason(source),
            "example": _example_label(report.nodeid),
        }
    )
    with open(_LIVE_RESULTS_PATH, "a", encoding="utf-8") as handle:
        handle.write(line + "\n")
        handle.flush()
        os.fsync(handle.fileno())


@pytest.fixture(scope="session")
def storage_state_path(browser) -> str | None:
    """Signs in once for the whole test session and reuses the resulting
    cookies/local storage for every test, instead of every single test
    signing in for itself -- the reuse pattern Playwright's own docs
    recommend for authenticated suites.

    Returns None when no test account is configured, so an unauthenticated
    application runs unauthenticated instead of failing to sign in to
    nothing.
    """
    if not has_credentials():
        return None

    _AUTH_STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    if not _AUTH_STATE_PATH.exists():
        from pages.login_page import LoginPage

        context = browser.new_context(base_url=BASE_URL)
        page = context.new_page()
        LoginPage(page).login(TEST_USERNAME, TEST_PASSWORD)
        context.storage_state(path=str(_AUTH_STATE_PATH))
        context.close()

    return str(_AUTH_STATE_PATH)


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, storage_state_path):
    return {
        **browser_context_args,
        "base_url": BASE_URL,
        "storage_state": storage_state_path,
    }
