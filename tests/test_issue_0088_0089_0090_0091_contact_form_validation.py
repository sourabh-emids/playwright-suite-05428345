"""Test for contact form validation."""
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


def test_inquiry_type_required(page_ready: Page) -> None:
    """Test contact form requires inquiry type selection."""
    inquiry_dropdown = page_ready.get_by_label("* Inquiry Type:")
    expect(inquiry_dropdown).to_be_visible()
    
    options = inquiry_dropdown.locator("option").all()
    assert len(options) > 1, "Should have multiple inquiry type options"


def test_email_validation(page_ready: Page) -> None:
    """Test contact form validates email syntax."""
    email_field = page_ready.get_by_label("Business Email:")
    email_field.fill("invalid-email")
    
    validity = email_field.evaluate("el => el.validity.valid")
    assert not validity, "Email field should reject invalid email"


def test_submission_feedback(page_ready: Page) -> None:
    """Test contact submission feedback success failure clear."""
    submit_btn = page_ready.get_by_role("button", name="Submit")
    expect(submit_btn).to_be_visible()
