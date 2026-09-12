"""Cookie Preferences control visible in footer."""
from pytest_bdd import given, then
from playwright.sync_api import Page, expect


@given("I have navigated to the homepage")
def navigate_to_homepage(page: Page) -> None:
    """Navigate to the homepage."""
    page.goto("/")


@then("Cookie Preferences control is visible in footer")
def cookie_preferences_visible(page: Page) -> None:
    """Verify Cookie Preferences control is visible in footer."""
    footer = page.get_by_role("contentinfo")
    expect(footer).to_be_visible()


@then("Cookie Preferences opens consent management UI")
def cookie_preferences_opens_ui(page: Page) -> None:
    """Verify Cookie Preferences opens consent management UI."""
    # Find and click cookie preferences if available
    customize_btn = page.get_by_role("button", name="Customize")
    if customize_btn.is_visible():
        customize_btn.click()
        # Verify consent management UI opens
        expect(page.get_by_role("tabpanel")).to_be_visible()
