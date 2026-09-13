"""Locators for Script failure resilience (issue_0054)."""
from playwright.sync_api import Locator, Page


class ScriptFailureLocators:
    """Locators for script failure resilience elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def header(self) -> Locator:
        return self.page.locator("header")

    @property
    def main_content(self) -> Locator:
        return self.page.locator("main")

    @property
    def footer(self) -> Locator:
        return self.page.locator("footer")

    @property
    def ctas(self) -> Locator:
        return self.page.locator("a[href*='/contact/']")
