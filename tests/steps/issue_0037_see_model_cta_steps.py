"""Step definitions for issue_0037: See the model CTA routes to FDCE detail page."""
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


@when("I click the See the model CTA")
def click_see_model_cta(page: Page) -> None:
    """Click the See the model CTA."""
    page.get_by_role("link", name="See the model").click()


@then("I should be routed to the FDCE detail page")
def routed_to_fdce_detail(page: Page) -> None:
    """Verify user is routed to FDCE detail page."""
    expect(page).to_have_url("https://www.emids.com/forward-deployed-context-engineering/")
