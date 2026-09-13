"""Locators for emids_lp_026-033: Insights section."""
from playwright.sync_api import Locator, Page


class EmidsLp026InsightsLocators:
    """Locators for Insights section verification."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def insights_section(self) -> Locator:
        return self.page.locator("section").filter(has=self.page.locator("text=Insights, text=Intelligence").first)

    @property
    def insight_cards(self) -> Locator:
        return self.insights_section.locator('[class*="card"], [class*="insight"]')

    @property
    def download_action(self) -> Locator:
        return self.page.locator('a:has-text("Download"), button:has-text("Download")')

    @property
    def read_more_action(self) -> Locator:
        return self.page.locator('a:has-text("Read More"), button:has-text("Read More")')

    @property
    def ebook_label(self) -> Locator:
        return self.page.locator('text=eBook, [class*="tag"]:has-text("eBook")')

    @property
    def blog_label(self) -> Locator:
        return self.page.locator('text=Blog, [class*="tag"]:has-text("Blog")')
