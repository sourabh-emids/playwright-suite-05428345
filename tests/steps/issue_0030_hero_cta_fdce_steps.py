"""Step definitions for issue_0030: Hero CTA routes to FDCE page."""
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


@when("I click the Hero CTA")
def click_hero_cta(page: Page) -> None:
    """Click the Hero CTA."""
    page.get_by_role("link", name="See How We Deliver Outcomes").click()


@then("I should be routed to the FDCE page")
def routed_to_fdce(page: Page) -> None:
    """Verify user is routed to FDCE page."""
    expect(page).to_have_url("https://www.emids.com/forward-deployed-context-engineering/")
