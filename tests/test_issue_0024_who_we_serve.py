"""Test for issue_0024 - Five audience entries rendering and Explore actions."""
import pytest

from pages.issue_0024_who_we_serve_page import Issue0024WhoWeServePage


@pytest.fixture
def who_we_serve_page(page) -> Issue0024WhoWeServePage:
    """Create page object for issue_0024 tests."""
    return Issue0024WhoWeServePage(page)
