"""Test for issue_0043 - Wistia embeds conditional loading."""
import pytest

from pages.issue_0043_wistia_embeds_page import Issue0043WistiaEmbedsPage


@pytest.fixture
def wistia_embeds_page(page) -> Issue0043WistiaEmbedsPage:
    """Create page object for issue_0043 tests."""
    return Issue0043WistiaEmbedsPage(page)
