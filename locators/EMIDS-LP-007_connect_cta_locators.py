"""Locators for Header Connect CTA - EMIDS-LP-007"""
from playwright.sync_api import Page, Locator


class ConnectCTALocators:
    """Locators for Connect CTA elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def header_connect_cta(self) -> Locator:
        return self.page.get_by_role("link", name="Connect").first

    @property
    def footer_connect_cta(self) -> Locator:
        return self.page.get_by_role("contentinfo").get_by_role("link", name="Connect")
