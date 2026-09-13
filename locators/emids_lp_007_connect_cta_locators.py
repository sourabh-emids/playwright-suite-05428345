"""Locators for emids_lp_007: Provide header Connect CTA."""
from playwright.sync_api import Locator, Page


class ConnectCTALocators:
    """Connect CTA locators."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def header_connect_cta(self) -> Locator:
        """Connect CTA in header banner."""
        return self.page.get_by_role("banner").get_by_role("link", name="Connect")

    @property
    def footer_connect_cta(self) -> Locator:
        """Connect CTA in footer."""
        return self.page.get_by_role("contentinfo").get_by_role("link", name="Connect")

    @property
    def all_connect_ctas(self) -> Locator:
        """All Connect CTAs on page."""
        return self.page.get_by_role("link", name="Connect")

    @property
    def main_connect_cta(self) -> Locator:
        """Primary Connect CTA (in header)."""
        return self.header_connect_cta
