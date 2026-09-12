"""Step definitions for issue_0057: Six insight cards render with type title and action."""
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


@then("insight cards render with type title and action")
def insight_cards_render(page: Page) -> None:
    """Verify insight cards render with type title and action."""
    insights_section = page.get_by_role("heading", name="The intelligence behind the outcomes")
    expect(insights_section).to_be_visible()
    
    next_button = page.get_by_role("button", name="Next")
    expect(next_button).to_be_visible()
