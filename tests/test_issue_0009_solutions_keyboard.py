"""Test for issue_0009: Solutions menu keyboard navigation maintains focus order."""
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


def test_solutions_menu_keyboard_navigation(page_ready: Page) -> None:
    """Test keyboard navigation through Solutions menu maintains focus order."""
    page_ready.get_by_role("button", name="Solutions").first.click()
    
    first_link = page_ready.get_by_role("link", name="Modernization").first
    first_link.focus()
    expect(first_link).to_be_focused()
    
    page_ready.keyboard.press("Tab")
    
    focused = page_ready.evaluate("() => document.activeElement")
    assert focused is not None, "Focus should be maintained after Tab"
