"""Step definitions for issue_0003 primary calls to action."""

from playwright.sync_api import Page
from pytest_bdd import given, parsers, then, when

from pages.issue_0003_primary_cta_page import PrimaryCallToActionPage


@given(
    "the homepage primary calls to action are available",
    target_fixture="cta_page",
)
def open_cta_page(page: Page) -> PrimaryCallToActionPage:
    cta_page = PrimaryCallToActionPage(page)
    cta_page.open()
    return cta_page


@when(
    parsers.parse(
        'the user selects the "{call_to_action}" call to action'
    )
)
def select_call_to_action(
    cta_page: PrimaryCallToActionPage,
    call_to_action: str,
) -> None:
    cta_page.select_call_to_action(call_to_action)


@then(
    parsers.parse(
        'the call-to-action path is "{path}" with heading "{heading}"'
    )
)
def verify_call_to_action_destination(
    cta_page: PrimaryCallToActionPage,
    path: str,
    heading: str,
) -> None:
    cta_page.assert_destination(path, heading)
