"""Locators for issue_0026: Insights section and cards render"""

from playwright.sync_api import Page, Locator


class Issue0026InsightsLocators:
    """Locators for Insights section."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def insights_section(self) -> Locator:
        """Returns the Insights section."""
        return self.page.get_by_role("heading", name="The intelligence behind the outcomes").locator("..")

    @property
    def insight_cards(self) -> Locator:
        """Returns insight cards."""
        return self.page.locator("[href*='/insights/']")
