"""Test for issue_0016 - All Solutions CTA visibility and routing."""
import pytest

from pages.issue_0016_all_solutions_cta_page import Issue0016AllSolutionsCTAPage


@pytest.fixture
def all_solutions_cta_page(page) -> Issue0016AllSolutionsCTAPage:
    """Create page object for issue_0016 tests."""
    return Issue0016AllSolutionsCTAPage(page)
