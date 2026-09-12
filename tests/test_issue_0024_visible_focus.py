"""Test for issue_0024: Visible focus maintained during navigation."""
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


def test_visible_focus_maintained(page_ready: Page) -> None:
    """Test visible focus is maintained on navigation items."""
    nav_link = page_ready.get_by_role("link", name="Solutions").first
    if not nav_link.is_visible():
        nav_link = page_ready.get_by_role("button", name="Solutions").first
    
    nav_link.focus()
    expect(nav_link).to_be_focused()
    expect(nav_link).to_be_visible()
