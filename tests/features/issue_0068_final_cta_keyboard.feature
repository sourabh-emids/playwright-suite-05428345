"""Final CTA primary action keyboard operable."""
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


@then("Final CTA primary action is keyboard operable")
def final_cta_keyboard_operable(page: Page) -> None:
    """Verify Final CTA primary action is keyboard operable."""
    final_cta_connect = page.get_by_role("link", name="Connect").last
    final_cta_connect.focus()
    expect(final_cta_connect).to_be_focused()
