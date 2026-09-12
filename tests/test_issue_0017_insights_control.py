"""Test for issue_0017: Insights control opens with child links readable."""
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


def test_insights_menu_opens(page_ready: Page) -> None:
    """Test Insights menu opens with child links readable."""
    page_ready.get_by_role("button", name="Insights").first.click()
    
    insights_header = page_ready.locator("text=Insights and Resources").first
    expect(insights_header).to_be_visible()
    
    child_links = [
        "Insights Hub",
        "Case Studies",
        "eBooks & Guides",
        "Webinars",
    ]
    
    for link_text in child_links:
        link = page_ready.get_by_role("link", name=link_text)
        expect(link).to_be_visible()
