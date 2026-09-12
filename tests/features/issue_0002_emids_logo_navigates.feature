"""Emids logo navigates to homepage."""
from pytest_bdd import given, when, then
from playwright.sync_api import Page, expect


@given("I am on any page")
def on_any_page(page: Page) -> None:
    """Navigate to the homepage."""
    page.goto("/")
    # Accept cookies
    try:
        page.get_by_role("button", name="Allow all").click()
    except Exception:
        pass


@when("I click the Emids logo")
def click_emids_logo(page: Page) -> None:
    """Click the Emids logo."""
    page.get_by_role("link", name="Emids logo").click()


@then("I should be on the homepage")
def on_homepage(page: Page) -> None:
    """Verify user is on the homepage."""
    expect(page).to_have_url("https://www.emids.com/")
