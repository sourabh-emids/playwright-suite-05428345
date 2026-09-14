"""Locators for the Company Navigation Group (issue_0006)."""
from playwright.sync_api import Locator, Page


class CompanyMenuLocators:
    """Locators for the Company menu component."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def company_trigger(self) -> Locator:
        return self.page.get_by_role("button", name="Company")

    @property
    def company_menu(self) -> Locator:
        return self.page.locator('[aria-label*="Company"], .company-menu')

    @property
    def about_us_label(self) -> Locator:
        return self.page.get_by_text("About Us")

    @property
    def connect_with_us_label(self) -> Locator:
        return self.page.get_by_text("Connect with Us")

    @property
    def contact_link(self) -> Locator:
        return self.page.get_by_role("link", name="Contact").or_(self.page.locator('a[href*="/contact/"]'))

    @property
    def company_links(self) -> Locator:
        return self.page.locator('.company-menu a')
