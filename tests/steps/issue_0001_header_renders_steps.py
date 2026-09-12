"""Step definitions for issue_0001: Header renders on initial page load."""
from pytest_bdd import given, then
from playwright.sync_api import Page, expect


@given("I navigate to the homepage")
def navigate_to_homepage(page: Page) -> None:
    """Navigate to the homepage."""
    page.goto("/")


@then("the header is visible")
def header_is_visible(page: Page) -> None:
    """Verify the header is visible."""
    header = page.get_by_role("banner").first
    expect(header).to_be_visible()
