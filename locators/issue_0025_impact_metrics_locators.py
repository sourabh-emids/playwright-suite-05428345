"""Locators for Impact proof metrics rendering (issue_0025)."""
from playwright.sync_api import Locator, Page


class ImpactMetricsLocators:
    """Locators for Impact metrics section elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def impact_section(self) -> Locator:
        return self.page.get_by_text("Impact")

    @property
    def years_experience(self) -> Locator:
        return self.page.get_by_text("36+ Years")

    @property
    def lives_touched(self) -> Locator:
        return self.page.get_by_text("Million Lives")

    @property
    def costs_saved(self) -> Locator:
        return self.page.get_by_text("Billion")
