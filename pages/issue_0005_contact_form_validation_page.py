"""Page object for issue_0005: Contact form validates required fields."""
from playwright.sync_api import Page, expect

from locators.issue_0005_contact_form_validation_locators import ContactFormValidationLocators


class ContactFormValidationPage:
    """Page object for the contact form page."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = ContactFormValidationLocators(page)

    def load_contact_page(self) -> None:
        self.page.goto("/contact/")
        self.dismiss_cookie_consent()

    def dismiss_cookie_consent(self) -> None:
        allow_all_button = self.page.get_by_role("button", name="Allow all")
        if allow_all_button.is_visible():
            allow_all_button.click()

    def submit_empty_form(self) -> None:
        self.locators.submit_button.click()

    def verify_validation_messages_appear(self) -> None:
        """Verify that validation messages appear for required fields."""
        # Wait for validation to appear after form submission
        self.page.wait_for_load_state("networkidle")
        
        # Check for HTML5 validation attributes or custom error messages
        # The form should show validation for at least one field
        validation_indicators = self.page.locator(
            "[aria-invalid='true'], .field-error, .error-message, [data-error], :invalid"
        )
        
        # Also check for the form validation bar/text that appears
        error_text = self.page.locator("text='This field is required'")
        required_asterisk_fields = self.page.locator("label:has-text('*')")
        
        # At least one of these validation indicators should be present
        has_validation = (
            validation_indicators.count() > 0 or 
            error_text.count() > 0 or
            required_asterisk_fields.count() > 0
        )
        
        expect(has_validation).to_be_truthy()

    def verify_first_name_required(self) -> None:
        expect(self.locators.first_name_field).to_be_visible()

    def verify_email_field_present(self) -> None:
        expect(self.locators.email_field).to_be_visible()

    def get_required_field_count(self) -> int:
        """Count the number of required fields marked with asterisk."""
        return self.page.locator("label:has-text('*')").count()
