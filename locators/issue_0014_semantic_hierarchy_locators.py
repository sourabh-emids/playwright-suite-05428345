"""Locators for Semantic section hierarchy (issue_0014)."""
from playwright.sync_api import Locator, Page


class SemanticHierarchyLocators:
    """Locators for semantic hierarchy elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def h1_elements(self) -> Locator:
        return self.page.locator("h1")

    @property
    def h2_elements(self) -> Locator:
        return self.page.locator("h2")

    @property
    def h3_elements(self) -> Locator:
        return self.page.locator("h3")

    @property
    def main_element(self) -> Locator:
        return self.page.locator("main")

    @property
    def header_element(self) -> Locator:
        return self.page.locator("header")

    @property
    def footer_element(self) -> Locator:
        return self.page.locator("footer")
