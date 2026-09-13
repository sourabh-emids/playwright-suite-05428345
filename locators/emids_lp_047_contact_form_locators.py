"""Locators for emids_lp_047-049: Contact form."""
from playwright.sync_api import Locator, Page


class EmidsLp047ContactFormLocators:
    """Locators for Contact form verification."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def contact_form(self) -> Locator:
        return self.page.locator("form")

    @property
    def first_name_field(self) -> Locator:
        return self.page.locator('input[name*="first"], input[name*="First"]').first

    @property
    def last_name_field(self) -> Locator:
        return self.page.locator('input[name*="last"], input[name*="Last"]').first

    @property
    def email_field(self) -> Locator:
        return self.page.locator('input[type="email"], input[name*="email"]').first

    @property
    def company_field(self) -> Locator:
        return self.page.locator('input[name*="company"], input[name*="Company"]').first

    @property
    def title_field(self) -> Locator:
        return self.page.locator('input[name*="title"], input[name*="Title"]').first

    @property
    def phone_field(self) -> Locator:
        return self.page.locator('input[type="tel"], input[name*="phone"]').first

    @property
    def inquiry_type_select(self) -> Locator:
        return self.page.locator('select[name*="inquiry"], select[name*="type"], select[id*="inquiry"]').first

    @property
    def comments_field(self) -> Locator:
        return self.page.locator('textarea[name*="comment"], textarea[name*="message"]').first

    @property
    def submit_button(self) -> Locator:
        return self.page.locator('button[type="submit"], input[type="submit"]').first
