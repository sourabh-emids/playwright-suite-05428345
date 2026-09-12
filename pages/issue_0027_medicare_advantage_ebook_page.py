"""Page object for issue_0027 - Medicare Advantage eBook card display."""
from playwright.sync_api import Page, expect

from locators.issue_0027_medicare_advantage_ebook_locators import Issue0027MedicareAdvantageEbookLocators


class Issue0027MedicareAdvantageEbookPage:
    """Page object for Medicare Advantage eBook card."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0027MedicareAdvantageEbookLocators()
        self.locators.page = page

    def view_insights_section(self) -> None:
        """Scroll to the Insights section."""
        self.locators.medicare_advantage_card.scroll_into_view_if_needed()

    def card_should_be_visible(self) -> None:
        """Verify card is visible."""
        expect(self.locators.medicare_advantage_card).to_be_visible()

    def card_should_have_ebook_indicator(self) -> None:
        """Verify card has eBook type indicator."""
        expect(self.page.locator("text=eBook").first).to_be_visible()

    def card_should_have_download_action(self) -> None:
        """Verify card has a download action."""
        expect(self.page.get_by_text("Download").first).to_be_visible()
