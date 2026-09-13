"""Page object for issue_0027-0033: Insight cards combined"""

from playwright.sync_api import Page, expect

from locators.issue_0027_0033_insight_cards_combined_locators import InsightCardsLocators


class InsightCardsPage:
    """Page object for Insight cards."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = InsightCardsLocators(page)

    def navigate_to_homepage(self) -> None:
        """Navigate to homepage."""
        self.page.goto("https://www.emids.com")

    def verify_insights_section(self) -> None:
        """Verify Insights section is visible."""
        expect(self.locators.insights_section).to_be_visible()

    def click_download_button(self) -> None:
        """Click a download button."""
        download = self.locators.download_buttons.first
        if download.count() > 0:
            download.click()

    def click_read_more_button(self) -> None:
        """Click a Read More button."""
        read_more = self.locators.read_more_buttons.first
        if read_more.count() > 0:
            read_more.click()
