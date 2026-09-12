"""Test for issue_0018: No empty menu groups in Insights."""
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


def test_insights_menu_no_empty_groups(page_ready: Page) -> None:
    """Test Insights menu has no empty groups."""
    page_ready.get_by_role("button", name="Insights").first.click()
    
    group_headers = [
        page_ready.locator("text=Insights and Resources"),
        page_ready.locator("text=News & Events"),
    ]
    
    for header in group_headers:
        expect(header).to_be_visible()
    
    # Verify each group has links
    links = ["Insights Hub", "Case Studies", "eBooks & Guides", "Webinars", "News"]
    for link_text in links:
        link = page_ready.get_by_role("link", name=link_text)
        expect(link).to_be_visible()
