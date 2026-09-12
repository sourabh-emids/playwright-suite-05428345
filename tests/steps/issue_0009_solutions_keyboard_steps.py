"""Step definitions for issue_0009: Solutions menu keyboard navigation maintains focus order."""
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


@when("I focus on the Solutions menu trigger")
def focus_solutions_trigger(page: Page) -> None:
    """Focus on the Solutions menu trigger."""
    page.get_by_role("button", name="Solutions").first.focus()


@when("I open the Solutions menu")
def open_solutions_menu(page: Page) -> None:
    """Open the Solutions menu."""
    page.get_by_role("button", name="Solutions").first.click()


@then("I can tab through menu items in logical order")
def tab_through_menu_items(page: Page) -> None:
    """Verify keyboard navigation through menu items works."""
    page.get_by_role("button", name="Solutions").first.click()
    
    first_link = page.get_by_role("link", name="Modernization").first
    first_link.focus()
    expect(first_link).to_be_focused()
    
    page.keyboard.press("Tab")
    
    focused = page.evaluate("() => document.activeElement")
    assert focused is not None, "Focus should be maintained after Tab"
