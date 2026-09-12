"""Test for issue_0029 - Life Sciences transformation eBook card display."""
import pytest

from pages.issue_0029_life_sciences_ebook_page import Issue0029LifeSciencesEbookPage


@pytest.fixture
def life_sciences_ebook_page(page) -> Issue0029LifeSciencesEbookPage:
    """Create page object for issue_0029 tests."""
    return Issue0029LifeSciencesEbookPage(page)
