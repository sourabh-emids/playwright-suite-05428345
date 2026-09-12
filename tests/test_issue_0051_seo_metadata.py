"""Test for issue_0051 - SEO metadata and crawlable structure."""
import pytest

from pages.issue_0051_seo_metadata_page import Issue0051SEOMetadataPage


@pytest.fixture
def seo_metadata_page(page) -> Issue0051SEOMetadataPage:
    """Create page object for issue_0051 tests."""
    return Issue0051SEOMetadataPage(page)
