"""Test for issue_0048 - Contact form Inquiry Type values."""
import pytest

from pages.issue_0048_contact_form_inquiry_type_page import Issue0048ContactFormInquiryTypePage


@pytest.fixture
def contact_form_inquiry_type_page(page) -> Issue0048ContactFormInquiryTypePage:
    """Create page object for issue_0048 tests."""
    return Issue0048ContactFormInquiryTypePage(page)
