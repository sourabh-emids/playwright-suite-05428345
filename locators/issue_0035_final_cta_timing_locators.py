"""Locators for 1 Day 2 Weeks 3 Months delivery message (issue_0035)."""
from playwright.sync_api import Locator, Page


class FinalCTATimingLocators:
    """Locators for Final CTA timing elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def timing_section(self) -> Locator:
        return self.page.get_by_text("1 Day · 2 Weeks · 3 Months")

    @property
    def day_label(self) -> Locator:
        return self.page.get_by_text("1 Day")

    @property
    def weeks_label(self) -> Locator:
        return self.page.get_by_text("2 Weeks")

    @property
    def months_label(self) -> Locator:
        return self.page.get_by_text("3 Months")
