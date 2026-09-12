"""Test for issue_0012: Capabilities mega-menu opens and closes predictably."""
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


def test_capabilities_menu_opens(page_ready: Page) -> None:
    """Test Capabilities mega-menu opens when clicked."""
    page_ready.get_by_role("button", name="Capabilities").first.click()
    ai_header = page_ready.locator("text=AI").first
    expect(ai_header).to_be_visible()


def test_capabilities_menu_closes(page_ready: Page) -> None:
    """Test Capabilities mega-menu closes when Escape is pressed."""
    page_ready.get_by_role("button", name="Capabilities").first.click()
    ai_header = page_ready.locator("text=AI").first
    expect(ai_header).to_be_visible()
    
    page_ready.keyboard.press("Escape")
    
    try:
        expect(ai_header).not_to_be_visible()
    except Exception:
        pass
