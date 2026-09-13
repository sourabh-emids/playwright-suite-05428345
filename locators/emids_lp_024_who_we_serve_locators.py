"""Locators for emids_lp_024: Who We Serve section."""
from playwright.sync_api import Locator, Page


class EmidsLp024WhoWeServeLocators:
    """Locators for Who We Serve section verification."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def who_we_serve_section(self) -> Locator:
        return self.page.locator("section").filter(has=self.page.locator("text=Payer, text=Provider").first)

    @property
    def audience_buttons(self) -> Locator:
        return self.page.locator('[class*="tab"], [class*="audience"] button, section button:has-text("Payer")')

    @property
    def payer_button(self) -> Locator:
        return self.page.locator('button:has-text("Payer")')

    @property
    def explore_cta(self) -> Locator:
        return self.page.locator('a:has-text("Explore")')
