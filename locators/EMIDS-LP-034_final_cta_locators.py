"""Locators for Final CTA section - EMIDS-LP-034, EMIDS-LP-035"""
from playwright.sync_api import Page, Locator


class FinalCTALocators:
    """Locators for Final CTA section elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def section(self) -> Locator:
        return self.page.get_by_text("From workshop to agent to scale deployment")

    @property
    def timeline_heading(self) -> Locator:
        return self.page.get_by_text("1 Day · 2 Weeks · 3 Months")

    @property
    def connect_cta(self) -> Locator:
        return self.page.locator("main").get_by_role("link", name="Connect").first

    @property
    def day_label(self) -> Locator:
        return self.page.get_by_text("1 Day")

    @property
    def weeks_label(self) -> Locator:
        return self.page.get_by_text("2 Weeks")

    @property
    def months_label(self) -> Locator:
        return self.page.get_by_text("3 Months")
