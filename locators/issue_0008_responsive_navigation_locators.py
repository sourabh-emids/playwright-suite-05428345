"""Locators for Responsive and accessible navigation behavior (issue_0008)."""
from playwright.sync_api import Locator, Page


class ResponsiveNavigationLocators:
    """Locators for responsive navigation elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def header(self) -> Locator:
        return self.page.locator("header")

    @property
    def nav_buttons(self) -> Locator:
        return self.page.locator("header button")

    @property
    def nav_links(self) -> Locator:
        return self.page.locator("header a")

    @property
    def solutions_button(self) -> Locator:
        return self.page.get_by_role("button", name="Solutions")
