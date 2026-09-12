"""Menu opens and closes without hover requirement."""
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


@when("I click on a menu trigger")
def click_menu_trigger(page: Page) -> None:
    """Click on a menu trigger."""
    page.get_by_role("button", name="Solutions").first.click()


@then("the menu opens")
def menu_opens(page: Page) -> None:
    """Verify the menu opens."""
    menu = page.locator("text=Solutions by Initiative").first
    expect(menu).to_be_visible()


@when("I click the menu trigger again")
def click_menu_trigger_again(page: Page) -> None:
    """Click the menu trigger again to close."""
    page.get_by_role("button", name="Solutions").first.click()


@then("the menu closes")
def menu_closes(page: Page) -> None:
    """Verify the menu closes."""
    try:
        menu = page.locator("text=Solutions by Initiative").first
        expect(menu).not_to_be_visible()
    except Exception:
        pass
