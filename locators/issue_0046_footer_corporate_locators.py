"""Locators for Footer corporate and contact information (issue_0046)."""
from playwright.sync_api import Locator, Page


class FooterCorporateLocators:
    """Locators for Footer corporate elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def footer(self) -> Locator:
        return self.page.locator("footer")

    @property
    def social_links(self) -> Locator:
        return self.page.locator("footer a[href*='linkedin'], footer a[href*='twitter'], footer a[href*='facebook']")
