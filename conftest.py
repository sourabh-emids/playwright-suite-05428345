"""Shared fixtures: base_url wiring and one-time authenticated session reuse.

Do not hand-edit tests/features/ or tests/steps/ -- regenerate the suite
instead. This file, utils/, and pages/base_page.py are yours to customize.
"""
from pathlib import Path

import pytest

from utils.config import BASE_URL, TEST_USERNAME, TEST_PASSWORD, has_credentials

_AUTH_STATE_PATH = Path(__file__).parent / ".auth" / "state.json"


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
