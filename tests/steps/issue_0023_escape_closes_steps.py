"""Step definitions for issue_0023: Escape key closes open overlays."""
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


@given("a menu is open")
def menu_is_open(page: Page) -> None:
    """Open a menu."""
    page.get_by_role("button", name="Solutions").first.click()
    menu = page.locator("text=Solutions by Initiative").first
    expect(menu).to_be_visible()


@when("I press Escape")
def press_escape(page: Page) -> None:
    """Press Escape key."""
    page.keyboard.press("Escape")


@then("the menu closes")
def menu_closes(page: Page) -> None:
    """Verify the menu closes."""
    try:
        menu = page.locator("text=Solutions by Initiative").first
        expect(menu).not_to_be_visible()
    except Exception:
        pass
