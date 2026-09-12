"""Locators for issue_0026 - Insights section six content cards rendering."""
from playwright.sync_api import Locator


class Issue0026InsightsSectionLocators:
    """Locators for Insights section."""

    @property
    def insights_section(self) -> Locator:
        """Return the Insights section."""
        return self.page.locator("text=The intelligence behind the outcomes")

    @property
    def content_cards(self) -> Locator:
        """Return the content cards."""
        return self.insights_section.locator("..").locator("article, [class*='card']")
