"""Locators for the Insights Navigation Group (issue_0005)."""
from playwright.sync_api import Locator, Page


class InsightsMenuLocators:
    """Locators for the Insights menu component."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def insights_trigger(self) -> Locator:
        return self.page.get_by_role("button", name="Insights")

    @property
    def insights_menu(self) -> Locator:
        return self.page.locator('[aria-label*="Insights"], .insights-menu')

    @property
    def insights_label(self) -> Locator:
        return self.page.get_by_text("Insights")

    @property
    def child_links(self) -> Locator:
        return self.page.locator('.insights-menu a, [aria-label*="Insights"] a')
