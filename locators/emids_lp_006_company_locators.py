"""Locators for emids_lp_006: Implement Company navigation group."""
from playwright.sync_api import Locator, Page


class EmidsLp006CompanyLocators:
    """Locators for Company navigation verification."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def company_button(self) -> Locator:
        return self.page.get_by_role("button", name="Company")

    @property
    def company_menu(self) -> Locator:
        return self.page.locator('[role="menu"], .mega-menu').filter(has=self.page.get_by_role("button", name="Company"))

    @property
    def about_us_group(self) -> Locator:
        return self.page.locator("text=About Us").first

    @property
    def connect_with_us_group(self) -> Locator:
        return self.page.locator("text=Connect with Us").first
