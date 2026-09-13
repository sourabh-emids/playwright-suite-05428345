"""Locators for Analytics and media conditional loading (issues 0038-0042)."""
from playwright.sync_api import Locator, Page


class AnalyticsMediaLocators:
    """Locators for analytics and media elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def main_content(self) -> Locator:
        return self.page.locator("main")

    @property
    def header(self) -> Locator:
        return self.page.locator("header")

    @property
    def wistia_player(self) -> Locator:
        return self.page.locator(".wistia_loaded")
