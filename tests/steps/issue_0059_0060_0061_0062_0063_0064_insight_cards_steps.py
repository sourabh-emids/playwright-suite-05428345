"""Step definitions for insight cards display."""
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


@then("Payer data readiness blog card displays with Read More")
def payer_blog_card_display(page: Page) -> None:
    """Verify Payer data readiness blog card displays with Read More."""
    page.goto("/insights/")
    read_more = page.get_by_role("link", name="Read More")
    expect(read_more).to_be_visible()
