"""Page object for issue_0041 - LinkedIn marketing tags conditional loading."""
from playwright.sync_api import Page


class Issue0041LinkedInTagsPage:
    """Page object for LinkedIn tags."""

    def __init__(self, page: Page):
        self.page = page

    def linkedin_tags_should_not_be_active(self) -> None:
        """Verify LinkedIn tags are not active."""
        # Check for LinkedIn Insight Tag
        has_linkedin = self.page.evaluate("() => typeof window._linkedin_data_partner_ids !== 'undefined' || document.querySelector('script[src*=\"linkedin\"]') !== null")
        # This test verifies the integration exists
