"""Test for issue_0005 - Insights navigation group accessibility."""
import pytest

from pages.issue_0005_insights_page import Issue0005InsightsMenuPage


@pytest.fixture
def insights_menu_page(page) -> Issue0005InsightsMenuPage:
    """Create page object for issue_0005 tests."""
    return Issue0005InsightsMenuPage(page)
