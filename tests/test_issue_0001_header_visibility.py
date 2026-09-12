"""Test for issue_0001 - Header visibility and global navigation."""
import pytest

from pages.issue_0001_header_page import Issue0001HeaderPage


@pytest.fixture
def issue_0001_page(page: Page) -> Issue0001HeaderPage:
    """Create page object for issue_0001 tests."""
    return Issue0001HeaderPage(page)
