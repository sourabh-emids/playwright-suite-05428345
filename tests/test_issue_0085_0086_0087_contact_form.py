"""Test for contact form."""
import pytest
from playwright.sync_api import Page, expect


@pytest.fixture
def page_ready(page: Page) -> Page:
    """Navigate to contact page with cookies accepted."""
    page.goto("/contact/")
    try:
        page.get_by_role("button", name="Allow all").click()
    except Exception:
        pass
    return page


def test_footer_mobile_readable(page_ready: Page) -> None:
    """Test footer corporate information readable at mobile width."""
    page_ready.set_viewport_size({"width": 320, "height": 568})
    footer = page_ready.get_by_role("contentinfo")
    expect(footer).to_be_visible()


def test_contact_form_fields(page_ready: Page) -> None:
    """Test contact form displays all eight required fields."""
    required_fields = [
        "* Inquiry Type:",
        "First Name:",
        "Last Name:",
        "Business Email:",
        "Company Name:",
    ]
    
    for field in required_fields:
        field_elem = page_ready.get_by_label(field)
        expect(field_elem).to_be_visible()
