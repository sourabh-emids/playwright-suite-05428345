"""Test for issue_0015 - Six featured solutions rendering and numbering."""
import pytest

from pages.issue_0015_featured_solutions_page import Issue0015FeaturedSolutionsPage


@pytest.fixture
def featured_solutions_page(page) -> Issue0015FeaturedSolutionsPage:
    """Create page object for issue_0015 tests."""
    return Issue0015FeaturedSolutionsPage(page)
