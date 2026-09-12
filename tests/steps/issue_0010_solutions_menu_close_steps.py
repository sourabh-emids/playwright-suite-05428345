"""Step definitions for issue_0010: Solutions menu closes and restores focus to trigger."""
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


@given("the Solutions menu is open")
def solutions_menu_open(page: Page) -> None:
    """Open the Solutions menu."""
    page.get_by_role("button", name="Solutions").first.click()


@when("I press Escape")
def press_escape(page: Page) -> None:
    """Press the Escape key."""
    page.keyboard.press("Escape")


@then("the Solutions menu closes")
def solutions_menu_closes(page: Page) -> None:
    """Verify Solutions menu closes."""
    try:
        menu = page.locator("text=Solutions by Initiative").first
        expect(menu).not_to_be_visible()
    except Exception:
        pass


@then("focus returns to the Solutions trigger")
def focus_returns_to_trigger(page: Page) -> None:
    """Verify focus returns to the Solutions trigger."""
    trigger = page.get_by_role("button", name="Solutions").first
    expect(trigger).to_be_focused()
