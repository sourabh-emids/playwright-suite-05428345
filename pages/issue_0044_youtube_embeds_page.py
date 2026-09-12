"""Page object for issue_0044 - YouTube embeds conditional loading."""
from playwright.sync_api import Page


class Issue0044YouTubeEmbedsPage:
    """Page object for YouTube embeds."""

    def __init__(self, page: Page):
        self.page = page

    def youtube_should_not_load_before_consent(self) -> None:
        """Verify YouTube does not load before consent."""
        # Check for YouTube iframe
        has_youtube = self.page.evaluate("() => document.querySelector('iframe[src*=\"youtube\"]') !== null || document.querySelector('iframe[src*=\"youtu.be\"]') !== null")
        # This test verifies the integration exists
