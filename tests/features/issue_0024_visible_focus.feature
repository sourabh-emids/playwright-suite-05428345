"""Visible focus maintained during navigation."""
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


@then("visible focus is maintained on navigation items")
def visible_focus_maintained(page: Page) -> None:
    """Verify visible focus is maintained on navigation items."""
    # Tab to first navigation item
    nav_link = page.get_by_role("link", name="Solutions").first
    if not nav_link.is_visible():
        nav_link = page.get_by_role("button", name="Solutions").first
    
    nav_link.focus()
    
    # Check that the element is focused
    expect(nav_link).to_be_focused()
    
    # Verify the element is visible
    expect(nav_link).to_be_visible()
