"""Locators for tc_005 - Contact form validation messages."""
from playwright.sync_api import Locator, Page


class Tc005FormLocators:
    """Locators for contact form validation."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def first_name_field(self) -> Locator:
        """First name field."""
        return self.page.get_by_label("First Name:")

    @property
    def last_name_field(self) -> Locator:
        """Last name field."""
        return self.page.get_by_label("Last Name:")

    @property
    def work_email_field(self) -> Locator:
        """Work email field."""
        return self.page.get_by_label("Work Email Address:")

    @property
    def company_name_field(self) -> Locator:
        """Company name field."""
        return self.page.get_by_label("Company Name:")

    @property
    def title_field(self) -> Locator:
        """Job title field."""
        return self.page.get_by_label("Title:")

    @property
    def phone_field(self) -> Locator:
        """Phone number field."""
        return self.page.get_by_label("Phone Number:")

    @property
    def comments_field(self) -> Locator:
        """Comments/message field."""
        return self.page.get_by_label("Comments:")

    @property
    def inquiry_type_field(self) -> Locator:
        """Inquiry type dropdown."""
        return self.page.get_by_label("Inquiry Type:")

    @property
    def submit_button(self) -> Locator:
        """Submit button."""
        return self.page.get_by_role("button", name="Submit")

    @property
    def form_required_label(self) -> Locator:
        """Required field label."""
        return self.page.get_by_text("Required *")

    @property
    def validation_error_messages(self) -> Locator:
        """Validation error messages."""
        return self.page.locator('[class*="error"], [class*="validation"], [aria-invalid="true"], [class*="message"]')

    @property
    def character_count(self) -> Locator:
        """Character count indicator."""
        return self.page.locator('[class*="count"], [class*="remaining"]')

    def get_field_error(self, field_name: str) -> Locator:
        """Get error message for a specific field."""
        return self.page.locator(f'input[name*="{field_name}"], [aria-describedby*="{field_name}"]')
