"""Test for issue_0017 - Featured solutions responsive interaction."""
import pytest

from pages.issue_0017_featured_solutions_responsive_page import Issue0017FeaturedSolutionsResponsivePage


@pytest.fixture
def featured_solutions_responsive_page(page) -> Issue0017FeaturedSolutionsResponsivePage:
    """Create page object for issue_0017 tests."""
    return Issue0017FeaturedSolutionsResponsivePage(page)
