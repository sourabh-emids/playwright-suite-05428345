"""Locators for emids_lp_004: Implement Industries mega-menu."""
from playwright.sync_api import Locator, Page


class EmidsLp004IndustriesLocators:
    """Locators for Industries mega-menu verification."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def industries_button(self) -> Locator:
        return self.page.get_by_role("button", name="Industries")

    @property
    def industries_menu(self) -> Locator:
        return self.page.locator('[role="menu"], .mega-menu').filter(has=self.page.get_by_role("button", name="Industries"))

    @property
    def payer_link(self) -> Locator:
        return self.page.locator('a[href*="/segments/payer/"]')

    @property
    def provider_link(self) -> Locator:
        return self.page.locator('a[href*="/segments/provider/"]')

    @property
    def healthtech_link(self) -> Locator:
        return self.page.locator('a[href*="/segments/healthtech/"]')

    @property
    def life_sciences_link(self) -> Locator:
        return self.page.locator('a[href*="/segments/life-sciences/"]')

    @property
    def consumer_link(self) -> Locator:
        return self.page.locator('a[href*="/segments/consumer/"]')
