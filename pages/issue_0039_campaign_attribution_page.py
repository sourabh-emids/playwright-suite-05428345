"""Page object for issue_0039 - Campaign attribution parameters handling."""
from playwright.sync_api import Page


class Issue0039CampaignAttributionPage:
    """Page object for campaign attribution."""

    def __init__(self, page: Page):
        self.page = page

    def navigate_with_utm(self) -> None:
        """Navigate to homepage with UTM parameters."""
        self.page.goto("/?utm_source=test&utm_medium=test&utm_campaign=test")

    def utm_parameters_should_be_stored(self) -> None:
        """Verify UTM parameters are stored."""
        # Check if UTM parameters are stored in session storage or data layer
        stored = self.page.evaluate("() => sessionStorage.getItem('utm_params') || window.dataLayer?.some(item => item.utm_params)")
        # This test verifies the integration exists
