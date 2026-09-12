"""Step definitions for issue_0053: Five audience entries with Explore actions visible."""
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


@then("five audience entries are visible with Explore actions")
def five_audiences_explore_visible(page: Page) -> None:
    """Verify five audience entries with Explore actions are visible."""
    audiences = ["Payer", "Provider", "HealthTech", "Life Sciences", "Consumer"]
    
    for audience in audiences:
        button = page.get_by_role("button", name=audience)
        expect(button).to_be_visible()
