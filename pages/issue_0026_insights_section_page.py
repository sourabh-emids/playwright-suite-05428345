"""Page object for issue_0026 - Insights section six content cards rendering."""
from playwright.sync_api import Page, expect

from locators.issue_0026_insights_section_locators import Issue0026InsightsSectionLocators


class Issue0026InsightsSectionPage:
    """Page object for Insights section."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0026InsightsSectionLocators()
        self.locators.page = page

    def view_insights_section(self) -> None:
        """Scroll to the Insights section."""
        self.locators.insights_section.scroll_into_view_if_needed()

    def section_heading_should_be_correct(self) -> None:
        """Verify section heading is correct."""
        expect(self.locators.insights_section).to_be_visible()

    def six_content_cards_should_be_visible(self) -> None:
        """Verify six content cards are visible."""
        cards = self.locators.content_cards
        count = cards.count()
        assert count == 6, f"Expected 6 content cards, found {count}"
