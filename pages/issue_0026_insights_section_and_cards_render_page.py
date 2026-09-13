"""Page object for issue_0026: Insights section and cards render"""

from playwright.sync_api import Page, expect

from locators.issue_0026_insights_section_and_cards_render_locators import Issue0026InsightsLocators


class Issue0026InsightsPage:
    """Page object for Insights section."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0026InsightsLocators(page)

    def navigate_to_homepage(self) -> None:
        """Navigate to homepage."""
        self.page.goto("https://www.emids.com")

    def verify_insights_section(self) -> None:
        """Verify Insights section is visible."""
        expect(self.locators.insights_section).to_be_visible()

    def count_insight_cards(self) -> int:
        """Count insight cards."""
        return self.locators.insight_cards.count()

    def resize_to_viewport(self, width: int, height: int) -> None:
        """Resize viewport."""
        self.page.set_viewport_size({"width": width, "height": height})
