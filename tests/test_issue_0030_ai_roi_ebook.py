"""Test for issue_0030 - AI ROI eBook card display."""
import pytest

from pages.issue_0030_ai_roi_ebook_page import Issue0030AiroiEbookPage


@pytest.fixture
def ai_roi_ebook_page(page) -> Issue0030AiroiEbookPage:
    """Create page object for issue_0030 tests."""
    return Issue0030AiroiEbookPage(page)
