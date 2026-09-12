"""Step definitions for issue_0054: Audience Explore routes to canonical segment page."""
from pytest_bdd import given, when, then
from playwright.sync_api import Page, expect


@given("I have navigated to the homepage")
def navigate_to_homepage(page: Page) -> None:
    """Navigate to the homepage."""
    page.goto("/")
    try:
        page.get_by_role("button", name="Allow all").click()
    except Exception:
        pass


@when("I click the Payer audience Explore")
def click_payer_explore(page: Page) -> None:
    """Click the Payer audience Explore."""
    page.locator("text=Explore").first.click()


@then("I should be routed to the segment page")
def routed_to_segment_page(page: Page) -> None:
    """Verify user is routed to segment page."""
    current_url = page.url
    assert "/segments/" in current_url, f"Should be on segment page, got: {current_url}"
