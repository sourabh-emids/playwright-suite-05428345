"""Locators for issue_0014: Semantic section hierarchy"""

from playwright.sync_api import Page, Locator


class Issue0014SemanticHierarchyLocators:
    """Locators for semantic section hierarchy."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def main_landmark(self) -> Locator:
        """Returns the main landmark."""
        return self.page.get_by_role("main")

    @property
    def header_landmark(self) -> Locator:
        """Returns the header landmark."""
        return self.page.locator("header").first

    @property
    def footer_landmark(self) -> Locator:
        """Returns the footer landmark."""
        return self.page.locator("footer").first

    @property
    def nav_landmark(self) -> Locator:
        """Returns the navigation landmark."""
        return self.page.get_by_role("navigation").first
