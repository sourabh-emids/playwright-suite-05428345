"""Step definitions for issue_0003: All top-level navigation reachable via keyboard."""
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


@then("all top-level navigation items are keyboard accessible")
def nav_items_keyboard_accessible(page: Page) -> None:
    """Verify all top-level navigation items can be focused with keyboard."""
    nav_items = [
        "Solutions",
        "Capabilities",
        "Industries",
        "Insights",
        "Company",
    ]
    
    for item_name in nav_items:
        nav_link = page.get_by_role("link", name=item_name).first
        if not nav_link.is_visible():
            nav_link = page.get_by_role("button", name=item_name).first
        
        nav_link.focus()
        expect(nav_link).to_be_focused()
