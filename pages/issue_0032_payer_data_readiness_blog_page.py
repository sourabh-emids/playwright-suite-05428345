"""Page object for issue_0032 - Payer data readiness blog card display."""
from playwright.sync_api import Page, expect

from locators.issue_0032_payer_data_readiness_blog_locators import Issue0032PayerDataReadinessBlogLocators


class Issue0032PayerDataReadinessBlogPage:
    """Page object for Payer data readiness blog card."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0032PayerDataReadinessBlogLocators()
        self.locators.page = page

    def view_insights_section(self) -> None:
        """Scroll to the Insights section."""
        self.locators.payer_data_card.scroll_into_view_if_needed()

    def card_should_be_visible(self) -> None:
        """Verify card is visible."""
        expect(self.locators.payer_data_card).to_be_visible()
