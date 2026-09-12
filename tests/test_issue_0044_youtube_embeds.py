"""Test for issue_0044 - YouTube embeds conditional loading."""
import pytest

from pages.issue_0044_youtube_embeds_page import Issue0044YouTubeEmbedsPage


@pytest.fixture
def youtube_embeds_page(page) -> Issue0044YouTubeEmbedsPage:
    """Create page object for issue_0044 tests."""
    return Issue0044YouTubeEmbedsPage(page)
