"""Locators for emids_lp_025: Impact proof metrics."""
from playwright.sync_api import Locator, Page


class EmidsLp025ImpactLocators:
    """Locators for Impact metrics section verification."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def impact_section(self) -> Locator:
        return self.page.locator("section").filter(has=self.page.locator("text=36").first)

    @property
    def metric_values(self) -> Locator:
        return self.page.locator('[class*="metric"] span, [class*="stat"] span, section [class*="number"]')
