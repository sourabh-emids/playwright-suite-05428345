"""Step definitions for issue_0015: Industries menu contains all five audiences."""
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


@then("the Industries menu contains all five audiences")
def industries_menu_has_five_audiences(page: Page) -> None:
    """Verify Industries menu contains Payer, Provider, HealthTech, Life Sciences, Consumer."""
    page.get_by_role("button", name="Industries").first.click()
    
    audiences = ["Payer", "Provider", "Health Tech", "Life Sciences", "Consumer"]
    
    for audience in audiences:
        link = page.get_by_role("link", name=audience)
        expect(link).to_be_visible()
