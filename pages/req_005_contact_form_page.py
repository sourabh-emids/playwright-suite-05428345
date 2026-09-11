"""Page object for REQ-005: Contact form displays validation for required fields."""

from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from locators.req_005_contact_form_locators import Req005ContactFormLocators


class Req005ContactFormPage(BasePage):
    """Page object for contact form operations."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = Req005ContactFormLocators(page)

    def goto_contact_page(self, base_url: str) -> None:
        """Navigate to the contact page."""
        self.goto(f"{base_url}/contact/")

    def submit_empty_form(self) -> None:
        """Submit the contact form without filling any fields."""
        self.locators.submit_button.click()

    def verify_form_visible(self) -> None:
        """Verify the contact form is visible."""
        expect(self.locators.contact_form).to_be_visible()

    def verify_first_name_has_validation(self) -> None:
        """Verify First Name field shows validation message."""
        expect(self.locators.first_name_field).to_have_attribute("aria-invalid", "true", timeout=5000)

    def verify_last_name_has_validation(self) -> None:
        """Verify Last Name field shows validation message."""
        expect(self.locators.last_name_field).to_have_attribute("aria-invalid", "true", timeout=5000)

    def verify_work_email_has_validation(self) -> None:
        """Verify Work Email field shows validation message."""
        expect(self.locators.work_email_field).to_have_attribute("aria-invalid", "true", timeout=5000)

    def verify_company_name_has_validation(self) -> None:
        """Verify Company Name field shows validation message."""
        expect(self.locators.company_name_field).to_have_attribute("aria-invalid", "true", timeout=5000)

    def verify_title_has_validation(self) -> None:
        """Verify Title field shows validation message."""
        expect(self.locators.title_field).to_have_attribute("aria-invalid", "true", timeout=5000)

    def verify_phone_number_has_validation(self) -> None:
        """Verify Phone Number field shows validation message."""
        expect(self.locators.phone_number_field).to_have_attribute("aria-invalid", "true", timeout=5000)

    def verify_inquiry_type_has_validation(self) -> None:
        """Verify Inquiry Type dropdown shows validation message."""
        expect(self.locators.inquiry_type_dropdown).to_have_attribute("aria-invalid", "true", timeout=5000)

    def verify_comments_has_validation(self) -> None:
        """Verify Comments field shows validation message."""
        expect(self.locators.comments_field).to_have_attribute("aria-invalid", "true", timeout=5000)

    def verify_required_fields_indicator_visible(self) -> None:
        """Verify 'Required *' indicator is visible."""
        expect(self.locators.form_required_indicator).to_be_visible()

    def verify_send_message_heading_visible(self) -> None:
        """Verify 'Send us a message' heading is visible."""
        expect(self.locators.send_message_heading).to_be_visible()

    def verify_validation_messages_appear_for_all_required_fields(self) -> None:
        """Verify validation messages appear for all required fields after empty submission."""
        expect(self.locators.first_name_field).to_have_attribute("aria-invalid", "true", timeout=5000)
        expect(self.locators.last_name_field).to_have_attribute("aria-invalid", "true", timeout=5000)
        expect(self.locators.work_email_field).to_have_attribute("aria-invalid", "true", timeout=5000)
        expect(self.locators.company_name_field).to_have_attribute("aria-invalid", "true", timeout=5000)
        expect(self.locators.title_field).to_have_attribute("aria-invalid", "true", timeout=5000)
        expect(self.locators.phone_number_field).to_have_attribute("aria-invalid", "true", timeout=5000)
        expect(self.locators.inquiry_type_dropdown).to_have_attribute("aria-invalid", "true", timeout=5000)
        expect(self.locators.comments_field).to_have_attribute("aria-invalid", "true", timeout=5000)

    def verify_form_not_submitted(self) -> None:
        """Verify the form was not submitted (stays on contact page)."""
        expect(self.page).to_have_url("*contact*")
