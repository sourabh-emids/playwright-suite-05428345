"""Test for issue_0026 - Insights section six content cards rendering."""
import pytest

from pages.issue_0026_insights_section_page import Issue0026InsightsSectionPage


@pytest.fixture
def insights_section_page(page) -> Issue0026InsightsSectionPage:
    """Create page object for issue_0026 tests."""
    return Issue0026InsightsSectionPage(page)
