"""Test for issue_0047 - Contact form fields and accessibility."""
import pytest

from pages.issue_0047_contact_form_fields_page import Issue0047ContactFormFieldsPage


@pytest.fixture
def contact_form_fields_page(page) -> Issue0047ContactFormFieldsPage:
    """Create page object for issue_0047 tests."""
    return Issue0047ContactFormFieldsPage(page)
