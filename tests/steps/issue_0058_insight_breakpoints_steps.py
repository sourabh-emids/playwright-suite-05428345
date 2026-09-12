"""Step definitions for issue_0058: Insight cards accessible at all breakpoints."""
from pytest_bdd import given, then
from playwright.sync_api import Page, expect


@given("I have navigated to the homepage")
def navigate_to_homepage(page: Page) -> None:
    """Navigate to the homepage."""
    page.goto("/")
    try:
        page.get_by_role("button", name="Allow all").click()
    except Exception:
        pass


@then("insight cards are accessible at all breakpoints")
def insight_cards_all_breakpoints(page: Page) -> None:
    """Verify insight cards accessible at all breakpoints."""
    page.set_viewport_size({"width": 1280, "height": 720})
    insights_heading = page.get_by_role("heading", name="The intelligence behind the outcomes")
    expect(insights_heading).to_be_visible()
    
    page.set_viewport_size({"width": 768, "height": 1024})
    expect(insights_heading).to_be_visible()
    
    page.set_viewport_size({"width": 375, "height": 667})
    expect(insights_heading).to_be_visible()
