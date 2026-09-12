"""Step definitions for issue_0035: How We Deliver section renders in intended sequence."""
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


@then("How We Deliver section renders in intended sequence")
def how_we_deliver_sequence(page: Page) -> None:
    """Verify How We Deliver section renders in intended sequence."""
    how_we_deliver = page.locator("text=How We Deliver").first
    expect(how_we_deliver).to_be_visible()
    
    h2 = page.get_by_role("heading", name="Embedded healthcare expertise")
    h3 = page.get_by_role("heading", name="Forward-Deployed Context Engineering")
    see_model_cta = page.get_by_role("link", name="See the model")
    
    expect(h2).to_be_visible()
    expect(h3).to_be_visible()
    expect(see_model_cta).to_be_visible()
