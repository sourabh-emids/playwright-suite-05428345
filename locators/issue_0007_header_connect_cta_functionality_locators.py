"""Locators for issue_0007: Header Connect CTA functionality"""

from playwright.sync_api import Page, Locator


class Issue0007ConnectCTALocators:
    """Locators for the Header Connect CTA functionality."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def connect_cta(self) -> Locator:
        """Returns the Connect CTA link in the header."""
        return self.page.get_by_role("link", name="Connect").first

    @property
    def header(self) -> Locator:
        """Returns the header element."""
        return self.page.locator("header").first
