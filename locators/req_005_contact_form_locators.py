"""Locators for REQ-005: Contact form displays validation for required fields."""

from playwright.sync_api import Page, Locator


class Req005ContactFormLocators:
    """Locators for contact form elements."""

    def __init__(self, page: Page):
        self._page = page

    @property
    def contact_form(self) -> Locator:
        """Main contact form."""
        return self._page.locator("#mktoForm_1001")

    @property
    def first_name_field(self) -> Locator:
        """First Name input field."""
        return self._page.get_by_label("* First Name:")

    @property
    def last_name_field(self) -> Locator:
        """Last Name input field."""
        return self._page.get_by_label("* Last Name:")

    @property
    def work_email_field(self) -> Locator:
        """Work Email Address input field."""
        return self._page.get_by_label("* Work Email Address:")

    @property
    def company_name_field(self) -> Locator:
        """Company Name input field."""
        return self._page.get_by_label("* Company Name:")

    @property
    def title_field(self) -> Locator:
        """Title input field."""
        return self._page.get_by_label("* Title:")

    @property
    def phone_number_field(self) -> Locator:
        """Phone Number input field."""
        return self._page.get_by_label("* Phone Number:")

    @property
    def inquiry_type_dropdown(self) -> Locator:
        """Inquiry Type dropdown."""
        return self._page.get_by_label("* Inquiry Type:")

    @property
    def comments_field(self) -> Locator:
        """Comments textarea field."""
        return self._page.get_by_label("* Comments:")

    @property
    def submit_button(self) -> Locator:
        """Submit button."""
        return self._page.get_by_role("button", name="Submit")

    @property
    def validation_message(self) -> Locator:
        """Generic validation message locator."""
        return self._page.locator(".mktoRequired .mktoError .mktoErrorMsg, .mktoForm .mktoError .mktoErrorMsg, [aria-invalid='true'] + span")

    @property
    def first_name_validation(self) -> Locator:
        """Validation message for First Name field."""
        return self._page.locator("[aria-label='* First Name:'] + .mktoError .mktoErrorMsg, [aria-label='* First Name:'] ~ span")

    @property
    def last_name_validation(self) -> Locator:
        """Validation message for Last Name field."""
        return self._page.locator("[aria-label='* Last Name:'] + .mktoError .mktoErrorMsg, [aria-label='* Last Name:'] ~ span")

    @property
    def work_email_validation(self) -> Locator:
        """Validation message for Work Email field."""
        return self._page.locator("[aria-label='* Work Email Address:'] + .mktoError .mktoErrorMsg, [aria-label='* Work Email Address:'] ~ span")

    @property
    def company_name_validation(self) -> Locator:
        """Validation message for Company Name field."""
        return self._page.locator("[aria-label='* Company Name:'] + .mktoError .mktoErrorMsg, [aria-label='* Company Name:'] ~ span")

    @property
    def title_validation(self) -> Locator:
        """Validation message for Title field."""
        return self._page.locator("[aria-label='* Title:'] + .mktoError .mktoErrorMsg, [aria-label='* Title:'] ~ span")

    @property
    def phone_number_validation(self) -> Locator:
        """Validation message for Phone Number field."""
        return self._page.locator("[aria-label='* Phone Number:'] + .mktoError .mktoErrorMsg, [aria-label='* Phone Number:'] ~ span")

    @property
    def inquiry_type_validation(self) -> Locator:
        """Validation message for Inquiry Type field."""
        return self._page.locator("[aria-label='* Inquiry Type:'] + .mktoError .mktoErrorMsg, [aria-label='* Inquiry Type:'] ~ span")

    @property
    def comments_validation(self) -> Locator:
        """Validation message for Comments field."""
        return self._page.locator("[aria-label='* Comments:'] + .mktoError .mktoErrorMsg, [aria-label='* Comments:'] ~ span")

    @property
    def form_required_indicator(self) -> Locator:
        """Required fields indicator on form."""
        return self._page.locator("text='Required *'")

    @property
    def contact_heading(self) -> Locator:
        """Contact page heading."""
        return self._page.get_by_role("heading", name="Let's Connect")

    @property
    def send_message_heading(self) -> Locator:
        """Send us a message section heading."""
        return self._page.get_by_role("heading", name="Send us a message")

    @property
    def all_required_fields_with_validation(self) -> Locator:
        """All required fields that have validation messages after empty submission."""
        return self._page.locator("[aria-invalid='true'], .mktoFieldWrap.mktoHasError")
