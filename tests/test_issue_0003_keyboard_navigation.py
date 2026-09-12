"""Test for issue_0003: All top-level navigation reachable via keyboard."""
import pytest
from playwright.sync_api import Page, expect


@pytest.fixture
def page_ready(page: Page) -> Page:
    """Navigate to homepage with cookies accepted."""
    page.goto("/")
    try:
        page.get_by_role("button", name="Allow all").click()
    except Exception:
        pass
    return page


def test_top_level_navigation_keyboard_accessible(page_ready: Page) -> None:
    """Test all top-level navigation items are keyboard accessible."""
    nav_items = ["Solutions", "Capabilities", "Industries", "Insights", "Company"]
    
    for item_name in nav_items:
        nav_link = page_ready.get_by_role("link", name=item_name).first
        if not nav_link.is_visible():
            nav_link = page_ready.get_by_role("button", name=item_name).first
        
        nav_link.focus()
        expect(nav_link).to_be_focused()
