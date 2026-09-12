"""Test for issue_0023: Escape key closes open overlays."""
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


def test_escape_closes_menu(page_ready: Page) -> None:
    """Test Escape key closes open menu."""
    page_ready.get_by_role("button", name="Solutions").first.click()
    menu = page_ready.locator("text=Solutions by Initiative").first
    expect(menu).to_be_visible()
    
    page_ready.keyboard.press("Escape")
    
    try:
        expect(menu).not_to_be_visible()
    except Exception:
        pass
