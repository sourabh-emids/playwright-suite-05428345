"""Locators for emids_lp_001: Render global header and brand entry point."""
from playwright.sync_api import Locator, Page


class EmidsLp001HeaderLocators:
    """Locators for header verification."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def header(self) -> Locator:
        return self.page.locator("header")

    @property
    def logo(self) -> Locator:
        return self.page.get_by_role("link", name="Emids logo").or_(self.page.locator('[aria-label="Emids logo"]'))

    @property
    def nav_solutions(self) -> Locator:
        return self.page.get_by_role("button", name="Solutions")

    @property
    def nav_capabilities(self) -> Locator:
        return self.page.get_by_role("button", name="Capabilities")

    @property
    def nav_industries(self) -> Locator:
        return self.page.get_by_role("button", name="Industries")

    @property
    def nav_insights(self) -> Locator:
        return self.page.get_by_role("button", name="Insights")

    @property
    def nav_company(self) -> Locator:
        return self.page.get_by_role("button", name="Company")

    @property
    def connect_cta(self) -> Locator:
        return self.page.locator('header a[href*="/contact/"]').first

    @property
    def mobile_menu_button(self) -> Locator:
        return self.page.locator('[aria-label="Menu"], [aria-label="Open menu"]')

    @property
    def nav_items(self) -> Locator:
        return self.page.locator("header nav a, header nav button").or_(self.page.locator('header a[href*="/contact/"]'))
