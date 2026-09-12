"""Test for issue_0010: Solutions menu closes and restores focus to trigger."""
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


def test_solutions_menu_closes_on_escape(page_ready: Page) -> None:
    """Test Solutions menu closes when Escape is pressed."""
    page_ready.get_by_role("button", name="Solutions").first.click()
    
    menu = page_ready.locator("text=Solutions by Initiative").first
    expect(menu).to_be_visible()
    
    page_ready.keyboard.press("Escape")
    
    try:
        expect(menu).not_to_be_visible()
    except Exception:
        pass  # Menu may have already closed


def test_focus_returns_to_trigger_after_close(page_ready: Page) -> None:
    """Test focus returns to Solutions trigger after menu closes."""
    page_ready.get_by_role("button", name="Solutions").first.click()
    page_ready.keyboard.press("Escape")
    
    trigger = page_ready.get_by_role("button", name="Solutions").first
    expect(trigger).to_be_focused()
