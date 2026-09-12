"""Locators for Insights menu - EMIDS-LP-005"""
from playwright.sync_api import Page, Locator


class InsightsMenuLocators:
    """Locators for Insights menu elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def insights_nav(self) -> Locator:
        return self.page.get_by_role("navigation", name="Main Navigation").get_by_role("link", name="Insights")

    @property
    def insights_trigger(self) -> Locator:
        return self.page.get_by_role("button", name="Insights").first

    @property
    def insights_resources_group(self) -> Locator:
        return self.page.get_by_text("Insights and Resources")

    @property
    def news_events_group(self) -> Locator:
        return self.page.get_by_text("News & Events")

    @property
    def insights_links(self) -> Locator:
        return self.page.locator('a[href*="/insights/"]')
