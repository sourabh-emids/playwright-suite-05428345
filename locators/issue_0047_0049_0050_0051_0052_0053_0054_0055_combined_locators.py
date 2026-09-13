"""Locators for remaining issues combined"""

from playwright.sync_api import Page, Locator


class CombinedLocators:
    """Locators for all remaining modules."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def main_content(self) -> Locator:
        """Returns main content."""
        return self.page.get_by_role("main")

    @property
    def header(self) -> Locator:
        """Returns header."""
        return self.page.locator("header").first

    @property
    def footer(self) -> Locator:
        """Returns footer."""
        return self.page.locator("footer").first

    @property
    def contact_form(self) -> Locator:
        """Returns contact form."""
        return self.page.locator("form")

    @property
    def first_name_field(self) -> Locator:
        """Returns first name field."""
        return self.page.get_by_label("First Name")

    @property
    def last_name_field(self) -> Locator:
        """Returns last name field."""
        return self.page.get_by_label("Last Name")

    @property
    def email_field(self) -> Locator:
        """Returns email field."""
        return self.page.get_by_label("Email")

    @property
    def submit_button(self) -> Locator:
        """Returns submit button."""
        return self.page.get_by_role("button", name="Submit")
