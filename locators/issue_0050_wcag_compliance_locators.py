"""Locators for WCAG 2.1 AA compliance (issue_0050)."""
from playwright.sync_api import Locator, Page


class WCAGComplianceLocators:
    """Locators for WCAG compliance elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def header(self) -> Locator:
        return self.page.locator("header")

    @property
    def main(self) -> Locator:
        return self.page.locator("main")

    @property
    def footer(self) -> Locator:
        return self.page.locator("footer")

    @property
    def interactive_elements(self) -> Locator:
        return self.page.locator("button, a, input, select, textarea")
