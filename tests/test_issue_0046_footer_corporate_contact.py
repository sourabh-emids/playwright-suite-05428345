"""Test for issue_0046 - Footer corporate contact information rendering."""
import pytest

from pages.issue_0046_footer_corporate_contact_page import Issue0046FooterCorporateContactPage


@pytest.fixture
def footer_corporate_contact_page(page) -> Issue0046FooterCorporateContactPage:
    """Create page object for issue_0046 tests."""
    return Issue0046FooterCorporateContactPage(page)
