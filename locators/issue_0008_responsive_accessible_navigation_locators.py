"""Locators for issue_0008: Responsive accessible navigation"""

from playwright.sync_api import Page, Locator


class Issue0008ResponsiveNavLocators:
    """Locators for the responsive accessible navigation."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def solutions_nav_button(self) -> Locator:
        """Returns the Solutions navigation button."""
        return self.page.get_by_role("button", name="Solutions")

    @property
    def header(self) -> Locator:
        """Returns the header element."""
        return self.page.locator("header").first

    @property
    def main_content(self) -> Locator:
        """Returns the main content area."""
        return self.page.locator("main").first
