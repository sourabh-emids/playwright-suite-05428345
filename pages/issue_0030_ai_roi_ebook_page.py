"""Page object for issue_0030 - AI ROI eBook card display."""
from playwright.sync_api import Page, expect

from locators.issue_0030_ai_roi_ebook_locators import Issue0030AiroiEbookLocators


class Issue0030AiroiEbookPage:
    """Page object for AI ROI eBook card."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0030AiroiEbookLocators()
        self.locators.page = page

    def view_insights_section(self) -> None:
        """Scroll to the Insights section."""
        self.locators.ai_roi_card.scroll_into_view_if_needed()

    def card_should_be_visible(self) -> None:
        """Verify card is visible."""
        expect(self.locators.ai_roi_card).to_be_visible()
