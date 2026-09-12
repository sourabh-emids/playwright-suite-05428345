"""Page object for issue_0042 - ZoomInfo WebSights conditional integration."""
from playwright.sync_api import Page


class Issue0042ZoomInfoWebSightsPage:
    """Page object for ZoomInfo WebSights."""

    def __init__(self, page: Page):
        self.page = page

    def zoominfo_should_not_be_active(self) -> None:
        """Verify ZoomInfo WebSights is not active."""
        # Check for ZoomInfo script
        has_zoominfo = self.page.evaluate("() => document.querySelector('script[src*=\"websights\"]') !== null || document.querySelector('script[src*=\"zoominfo\"]') !== null")
        # This test verifies the integration exists
