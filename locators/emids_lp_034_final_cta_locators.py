"""Locators for emids_lp_034-035: Final CTA section."""
from playwright.sync_api import Locator, Page


class EmidsLp034FinalCtaLocators:
    """Locators for Final CTA section verification."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def final_cta_section(self) -> Locator:
        return self.page.locator("section").filter(has=self.page.locator("text=1 Day, text=2 Weeks, text=3 Months").first)

    @property
    def connect_cta(self) -> Locator:
        return self.final_cta_section.locator('a:has-text("Connect")').first

    @property
    def timing_message(self) -> Locator:
        return self.page.locator("text=1 Day · 2 Weeks · 3 Months")
