"""Locators for emids_lp_012-013: How We Deliver section."""
from playwright.sync_api import Locator, Page


class EmidsLp012HowWeDeliverLocators:
    """Locators for How We Deliver section verification."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def how_we_deliver_section(self) -> Locator:
        return self.page.locator("section, main > div").filter(has=self.page.locator("text=Forward-deployed context engineering"))

    @property
    def see_the_model_cta(self) -> Locator:
        return self.page.locator('a:has-text("See the model")').first

    @property
    def fdce_heading(self) -> Locator:
        return self.page.locator("text=Forward-Deployed Context Engineering").first

    @property
    def section_cta(self) -> Locator:
        return self.how_we_deliver_section.locator("a")
