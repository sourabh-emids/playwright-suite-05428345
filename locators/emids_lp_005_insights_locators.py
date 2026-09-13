"""Locators for emids_lp_005: Implement Insights navigation group."""
from playwright.sync_api import Locator, Page


class EmidsLp005InsightsLocators:
    """Locators for Insights navigation verification."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def insights_button(self) -> Locator:
        return self.page.get_by_role("button", name="Insights")

    @property
    def insights_menu(self) -> Locator:
        return self.page.locator('[role="menu"], .mega-menu').filter(has=self.page.get_by_role("button", name="Insights"))

    @property
    def insights_resources_group(self) -> Locator:
        return self.page.locator("text=Insights and Resources").first

    @property
    def news_events_group(self) -> Locator:
        return self.page.locator("text=News & Events").first
