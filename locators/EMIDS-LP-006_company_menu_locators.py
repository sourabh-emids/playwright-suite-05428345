"""Locators for Company menu - EMIDS-LP-006"""
from playwright.sync_api import Page, Locator


class CompanyMenuLocators:
    """Locators for Company menu elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def company_nav(self) -> Locator:
        return self.page.get_by_role("navigation", name="Main Navigation").get_by_role("link", name="Company")

    @property
    def company_trigger(self) -> Locator:
        return self.page.get_by_role("button", name="Company").first

    @property
    def about_us_group(self) -> Locator:
        return self.page.get_by_text("About Us")

    @property
    def connect_with_us_group(self) -> Locator:
        return self.page.get_by_text("Connect with Us")

    @property
    def company_links(self) -> Locator:
        return self.page.locator('a[href*="/about/"], a[href*="/contact/"]')
