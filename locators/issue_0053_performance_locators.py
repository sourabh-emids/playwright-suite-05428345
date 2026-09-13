"""Locators for Performance and Core Web Vitals goals (issue_0053)."""
from playwright.sync_api import Locator, Page


class PerformanceLocators:
    """Locators for performance elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def main_content(self) -> Locator:
        return self.page.locator("main")

    @property
    def images(self) -> Locator:
        return self.page.locator("img")

    @property
    def h1_heading(self) -> Locator:
        return self.page.locator("h1").first
