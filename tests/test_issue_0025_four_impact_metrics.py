"""Test for issue_0025 - Four impact proof metrics rendering."""
import pytest

from pages.issue_0025_four_impact_metrics_page import Issue0025FourImpactMetricsPage


@pytest.fixture
def four_impact_metrics_page(page) -> Issue0025FourImpactMetricsPage:
    """Create page object for issue_0025 tests."""
    return Issue0025FourImpactMetricsPage(page)
