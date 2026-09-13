"""Locators for issue_0006: Company navigation group"""

from playwright.sync_api import Page, Locator


class Issue0006CompanyMenuLocators:
    """Locators for the Company navigation group."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def company_nav_button(self) -> Locator:
        """Returns the Company navigation button."""
        return self.page.get_by_role("button", name="Company")

    @property
    def about_us_heading(self) -> Locator:
        """Returns the About Us heading."""
        return self.page.get_by_text("About Us")

    @property
    def connect_with_us_heading(self) -> Locator:
        """Returns the Connect with Us heading."""
        return self.page.get_by_text("Connect with Us")

    def get_all_company_links(self) -> Locator:
        """Returns all links in the Company menu."""
        return self.page.locator("button:has-text('Company') ~ a")
