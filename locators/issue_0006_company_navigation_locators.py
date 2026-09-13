"""Locators for Company navigation group implementation (issue_0006)."""
from playwright.sync_api import Locator, Page


class CompanyNavigationLocators:
    """Locators for Company navigation elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def company_button(self) -> Locator:
        return self.page.get_by_role("button", name="Company")

    @property
    def about_us_link(self) -> Locator:
        return self.page.get_by_text("About Us").first

    @property
    def connect_link(self) -> Locator:
        return self.page.get_by_text("Connect with Us").first

    @property
    def menu_visible(self) -> Locator:
        return self.page.get_by_text("About Us")
