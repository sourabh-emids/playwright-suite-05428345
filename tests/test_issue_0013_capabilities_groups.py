"""Test for issue_0013: Capabilities menu AI Engineering Platforms groups present."""
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


def test_capabilities_menu_has_three_groups(page_ready: Page) -> None:
    """Test Capabilities menu has AI, Engineering, and Platforms groups."""
    page_ready.get_by_role("button", name="Capabilities").first.click()
    
    ai_group = page_ready.locator("text=AI").first
    engineering_group = page_ready.locator("text=Engineering").first
    platforms_group = page_ready.locator("text=Platforms").first
    
    expect(ai_group).to_be_visible()
    expect(engineering_group).to_be_visible()
    expect(platforms_group).to_be_visible()
