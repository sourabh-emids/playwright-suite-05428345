"""Locators for issue_0037-0044: Analytics and Media combined"""

from playwright.sync_api import Page, Locator


class AnalyticsMediaLocators:
    """Locators for Analytics and Media Integration."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def main_content(self) -> Locator:
        """Returns the main content area."""
        return self.page.get_by_role("main")

    @property
    def header(self) -> Locator:
        """Returns the header."""
        return self.page.locator("header").first

    @property
    def footer(self) -> Locator:
        """Returns the footer."""
        return self.page.locator("footer").first
