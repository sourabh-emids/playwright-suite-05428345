"""Test for issue_0042 - ZoomInfo WebSights conditional integration."""
import pytest

from pages.issue_0042_zoominfo_websights_page import Issue0042ZoomInfoWebSightsPage


@pytest.fixture
def zoominfo_websights_page(page) -> Issue0042ZoomInfoWebSightsPage:
    """Create page object for issue_0042 tests."""
    return Issue0042ZoomInfoWebSightsPage(page)
