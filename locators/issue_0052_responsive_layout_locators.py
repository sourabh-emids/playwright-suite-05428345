"""Locators for Responsive layout across viewports (issue_0052)."""
from playwright.sync_api import Locator, Page


class ResponsiveLayoutLocators:
    """Locators for responsive layout elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def main_content(self) -> Locator:
        return self.page.locator("main")

    @property
    def images(self) -> Locator:
        return self.page.locator("img")
