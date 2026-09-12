"""Test for issue_0002 - Solutions mega-menu functionality."""
import pytest

from pages.issue_0002_solutions_page import Issue0002SolutionsMenuPage


@pytest.fixture
def solutions_menu_page(page) -> Issue0002SolutionsMenuPage:
    """Create page object for issue_0002 tests."""
    return Issue0002SolutionsMenuPage(page)
