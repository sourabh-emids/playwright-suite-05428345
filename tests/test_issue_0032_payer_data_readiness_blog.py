"""Test for issue_0032 - Payer data readiness blog card display."""
import pytest

from pages.issue_0032_payer_data_readiness_blog_page import Issue0032PayerDataReadinessBlogPage


@pytest.fixture
def payer_data_readiness_blog_page(page) -> Issue0032PayerDataReadinessBlogPage:
    """Create page object for issue_0032 tests."""
    return Issue0032PayerDataReadinessBlogPage(page)
