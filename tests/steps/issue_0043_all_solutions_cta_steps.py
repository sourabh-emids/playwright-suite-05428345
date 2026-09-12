"""Step definitions for issue_0043: All Solutions CTA routes to solutions portfolio."""
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


@when("I click the All solutions CTA")
def click_all_solutions_cta(page: Page) -> None:
    """Click the All solutions CTA."""
    page.get_by_role("link", name="All solutions").click()


@then("I should be routed to the solutions portfolio page")
def routed_to_solutions(page: Page) -> None:
    """Verify user is routed to solutions portfolio page."""
    expect(page).to_have_url("https://www.emids.com/solutions/")
