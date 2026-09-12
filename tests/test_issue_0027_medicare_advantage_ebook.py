"""Test for issue_0027 - Medicare Advantage eBook card display."""
import pytest

from pages.issue_0027_medicare_advantage_ebook_page import Issue0027MedicareAdvantageEbookPage


@pytest.fixture
def medicare_advantage_ebook_page(page) -> Issue0027MedicareAdvantageEbookPage:
    """Create page object for issue_0027 tests."""
    return Issue0027MedicareAdvantageEbookPage(page)
