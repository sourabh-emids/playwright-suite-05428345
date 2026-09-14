"""Locators for the Header Connect CTA (issue_0007)."""
from playwright.sync_api import Locator, Page


class ConnectCTALocators:
    """Locators for the Connect CTA component."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def connect_cta(self) -> Locator:
        return self.page.get_by_role("link", name="Connect").first

    @property
    def header(self) -> Locator:
        return self.page.locator("header")

    @property
    def contact_link(self) -> Locator:
        return self.page.get_by_role("link", name="Contact").or_(self.page.locator('a[href*="/contact/"]').first)

    @property
    def all_nav_links(self) -> Locator:
        return self.page.locator("header a")
