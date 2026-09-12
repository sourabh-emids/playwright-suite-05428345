"""Locators for Impact section - EMIDS-LP-025"""
from playwright.sync_api import Page, Locator


class ImpactLocators:
    """Locators for Impact section elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def section(self) -> Locator:
        return self.page.get_by_text("In healthcare, good intentions don't move the needle")

    @property
    def years_experience_metric(self) -> Locator:
        return self.page.get_by_text("Years Healthcare Experience")

    @property
    def lives_touched_metric(self) -> Locator:
        return self.page.get_by_text("Million Lives Touched")

    @property
    def costs_saved_metric(self) -> Locator:
        return self.page.get_by_text("Billion Medical Costs Saved")

    @property
    def platforms_launched_metric(self) -> Locator:
        return self.page.get_by_text("Platforms Launched")

    @property
    def all_metrics(self) -> Locator:
        return self.page.locator(".impact-metrics span, .metrics span, section:has-text('Impact') span")
