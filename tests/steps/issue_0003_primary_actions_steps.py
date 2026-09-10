"""Step bindings for issue_0003 primary actions."""

from playwright.sync_api import Page
from pytest_bdd import given, parsers, then, when

from pages.issue_0003_primary_actions_page import PrimaryActionsPage


@given(
    "the Emids homepage is open for primary actions",
    target_fixture="primary_actions_page",
)
def open_homepage(page: Page) -> PrimaryActionsPage:
    actions_page = PrimaryActionsPage(page)
    actions_page.open()
    return actions_page


@when(parsers.parse('the user selects the "{action}" primary action'))
def select_primary_action(
    primary_actions_page: PrimaryActionsPage,
    action: str,
) -> None:
    primary_actions_page.select_action(action)


@then(parsers.parse('the browser opens the action path "{path}"'))
def verify_action_path(
    primary_actions_page: PrimaryActionsPage,
    path: str,
) -> None:
    primary_actions_page.verify_path(path)
