"""Connect CTA routes to HTTPS contact page."""
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


@when("I click the Connect CTA")
def click_connect_cta(page: Page) -> None:
    """Click the Connect CTA."""
    page.get_by_role("link", name="Connect").first.click()


@then("I should be on an HTTPS contact page")
def on_https_contact_page(page: Page) -> None:
    """Verify user is on an HTTPS contact page."""
    expect(page).to_have_url("https://www.emids.com/contact/")
