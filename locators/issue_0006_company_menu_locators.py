"""Locators for issue_0006 - Company navigation group keyboard and touch access."""
from playwright.sync_api import Locator


class Issue0006CompanyMenuLocators:
    """Locators for Company navigation group."""

    @property
    def company_nav_button(self) -> Locator:
        """Return the Company navigation button."""
        return self.page.locator('button:has-text("Company")')

    @property
    def about_us_header(self) -> Locator:
        """Return the 'About Us' header."""
        return self.page.locator("text=About Us").first

    @property
    def connect_with_us_header(self) -> Locator:
        """Return the 'Connect with Us' header."""
        return self.page.locator("text=Connect with Us")
