"""Connect CTA routes to contact experience."""
from pytest_bdd import given, when, then
from playwright.sync_api import Page, expect


@given("I am on the homepage")
def on_homepage(page: Page) -> None:
    """Navigate to the homepage."""
    page.goto("/")
    try:
        page.get_by_role("button", name="Allow all").click()
    except Exception:
        pass


@when("I click the Connect CTA in the header")
def click_connect_cta(page: Page) -> None:
    """Click the Connect CTA."""
    page.get_by_role("link", name="Connect").first.click()


@then("I should be routed to the contact page")
def routed_to_contact(page: Page) -> None:
    """Verify user is on the contact page."""
    expect(page).to_have_url("https://www.emids.com/contact/")
