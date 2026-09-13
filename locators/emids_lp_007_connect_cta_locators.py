"""Locators for emids_lp_007: Provide header Connect CTA."""
from playwright.sync_api import Locator, Page


class EmidsLp007ConnectCtaLocators:
    """Locators for Connect CTA verification."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def connect_cta_header(self) -> Locator:
        return self.page.locator('header a[href*="/contact/"]').first

    @property
    def connect_cta_all(self) -> Locator:
        return self.page.locator('a:has-text("Connect"), button:has-text("Connect")')

    @property
    def footer_connect_cta(self) -> Locator:
        return self.page.locator('footer a[href*="/contact/"]')
