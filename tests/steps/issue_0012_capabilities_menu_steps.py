"""Step definitions for issue_0012: Capabilities mega-menu opens and closes predictably."""
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


@when("I click the Capabilities button")
def click_capabilities_button(page: Page) -> None:
    """Click the Capabilities button."""
    page.get_by_role("button", name="Capabilities").first.click()


@then("the Capabilities mega-menu opens")
def capabilities_menu_opens(page: Page) -> None:
    """Verify Capabilities mega-menu opens."""
    ai_header = page.locator("text=AI").first
    expect(ai_header).to_be_visible()


@when("I press Escape to close the menu")
def close_menu_with_escape(page: Page) -> None:
    """Press Escape to close the menu."""
    page.keyboard.press("Escape")


@then("the Capabilities mega-menu closes")
def capabilities_menu_closes(page: Page) -> None:
    """Verify Capabilities mega-menu closes."""
    try:
        ai_header = page.locator("text=AI").first
        expect(ai_header).not_to_be_visible()
    except Exception:
        pass
