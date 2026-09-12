"""Test for issue_0008: Solutions mega-menu opens with all links selectable."""
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


def test_solutions_menu_opens(page_ready: Page) -> None:
    """Test Solutions mega-menu opens when clicked."""
    page_ready.get_by_role("button", name="Solutions").first.click()
    menu = page_ready.locator("text=Solutions by Initiative").first
    expect(menu).to_be_visible()


def test_solutions_menu_links_selectable(page_ready: Page) -> None:
    """Test all links in Solutions menu are selectable."""
    page_ready.get_by_role("button", name="Solutions").first.click()
    
    expected_links = [
        "Modernization",
        "Interoperability",
        "Cloud Transformation",
        "Agentic AI",
        "Global Capability Center",
    ]
    
    for link_text in expected_links:
        link = page_ready.get_by_role("link", name=link_text).first
        expect(link).to_be_visible()
        href = link.get_attribute("href")
        assert href is not None and href != "", f"Link {link_text} should have valid href"
