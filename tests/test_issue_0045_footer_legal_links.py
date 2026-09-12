"""Test for issue_0045 - Footer legal navigation links."""
import pytest

from pages.issue_0045_footer_legal_links_page import Issue0045FooterLegalLinksPage


@pytest.fixture
def footer_legal_links_page(page) -> Issue0045FooterLegalLinksPage:
    """Create page object for issue_0045 tests."""
    return Issue0045FooterLegalLinksPage(page)
