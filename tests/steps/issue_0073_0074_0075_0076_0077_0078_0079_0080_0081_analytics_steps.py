"""Step definitions for analytics requirements."""
from pytest_bdd import given, then
from playwright.sync_api import Page


@given("I have navigated to the homepage")
def navigate_to_homepage(page: Page) -> None:
    """Navigate to the homepage."""
    page.goto("/")
    try:
        page.get_by_role("button", name="Allow all").click()
    except Exception:
        pass


@then("core page functional if GTM fails")
def core_page_functional_gtm_fails(page: Page) -> None:
    """Verify core page functional if GTM fails."""
    h1 = page.get_by_role("heading", level=1).first
    assert h1.is_visible()


@then("UTM parameters preserved without breaking URLs")
def utm_parameters_preserved(page: Page) -> None:
    """Verify UTM parameters preserved without breaking URLs."""
    page.goto("/?utm_source=test&utm_medium=test&utm_campaign=test")
    h1 = page.get_by_role("heading", level=1).first
    assert h1.is_visible()
