"""Test for issue_0038 - Google Analytics post-consent measurement."""
import pytest

from pages.issue_0038_google_analytics_page import Issue0038GoogleAnalyticsPage


@pytest.fixture
def google_analytics_page(page) -> Issue0038GoogleAnalyticsPage:
    """Create page object for issue_0038 tests."""
    return Issue0038GoogleAnalyticsPage(page)
