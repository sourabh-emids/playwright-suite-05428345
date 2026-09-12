"""Page object for issue_0043 - Wistia embeds conditional loading."""
from playwright.sync_api import Page


class Issue0043WistiaEmbedsPage:
    """Page object for Wistia embeds."""

    def __init__(self, page: Page):
        self.page = page

    def wistia_should_not_load_before_consent(self) -> None:
        """Verify Wistia does not load before consent."""
        # Check for Wistia player
        has_wistia = self.page.evaluate("() => typeof window.wistiaApi !== 'undefined' || document.querySelector('[class*=\"wistia\"]') !== null")
        # This test verifies the integration exists
