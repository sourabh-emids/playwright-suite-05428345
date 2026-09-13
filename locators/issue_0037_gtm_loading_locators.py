"""Locators for Google Tag Manager container loading (issue_0037)."""
from playwright.sync_api import Locator, Page


class GTMLoadingLocators:
    """Locators for GTM loading elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def main_content(self) -> Locator:
        return self.page.locator("main")

    @property
    def header(self) -> Locator:
        return self.page.locator("header")
