"""Locators for Insights navigation group implementation (issue_0005)."""
from playwright.sync_api import Locator, Page


class InsightsNavigationLocators:
    """Locators for Insights navigation elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def insights_button(self) -> Locator:
        return self.page.get_by_role("button", name="Insights")

    @property
    def insights_resources_link(self) -> Locator:
        return self.page.get_by_text("Insights and Resources").first

    @property
    def news_events_link(self) -> Locator:
        return self.page.get_by_text("News & Events").first

    @property
    def menu_visible(self) -> Locator:
        return self.page.get_by_text("Insights and Resources")
