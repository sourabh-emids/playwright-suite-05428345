"""Locators for Header Connect CTA functionality (issue_0007)."""
from playwright.sync_api import Locator, Page


class HeaderConnectCTALocators:
    """Locators for Header Connect CTA elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def connect_cta(self) -> Locator:
        return self.page.get_by_role("link", name="Connect").first

    @property
    def header(self) -> Locator:
        return self.page.locator("header")

    @property
    def connect_ctas(self) -> Locator:
        return self.page.get_by_role("link", name="Connect").all()
