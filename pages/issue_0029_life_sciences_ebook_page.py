"""Page object for issue_0029 - Life Sciences transformation eBook card display."""
from playwright.sync_api import Page, expect

from locators.issue_0029_life_sciences_ebook_locators import Issue0029LifeSciencesEbookLocators


class Issue0029LifeSciencesEbookPage:
    """Page object for Life Sciences eBook card."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0029LifeSciencesEbookLocators()
        self.locators.page = page

    def view_insights_section(self) -> None:
        """Scroll to the Insights section."""
        self.locators.life_sciences_card.scroll_into_view_if_needed()

    def card_should_be_visible(self) -> None:
        """Verify card is visible."""
        expect(self.locators.life_sciences_card).to_be_visible()
