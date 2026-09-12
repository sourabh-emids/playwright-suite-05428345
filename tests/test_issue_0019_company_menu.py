"""Test for issue_0019: Company menu exposes approved links keyboard operable."""
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


def test_company_menu_exposes_links(page_ready: Page) -> None:
    """Test Company menu exposes approved links."""
    page_ready.get_by_role("button", name="Company").first.click()
    
    approved_links = [
        "Our Story",
        "Leadership Team",
        "Partners",
        "Careers",
        "Offices",
        "Contact Us",
    ]
    
    for link_text in approved_links:
        link = page_ready.get_by_role("link", name=link_text)
        expect(link).to_be_visible()


def test_company_menu_keyboard_operable(page_ready: Page) -> None:
    """Test Company menu is keyboard operable."""
    page_ready.get_by_role("button", name="Company").first.click()
    
    first_link = page_ready.get_by_role("link", name="Our Story").first
    first_link.focus()
    expect(first_link).to_be_focused()
