"""Page object for issue_0048 - Contact form Inquiry Type values."""
from playwright.sync_api import Page, expect

from locators.issue_0048_contact_form_inquiry_type_locators import Issue0048ContactFormInquiryTypeLocators


class Issue0048ContactFormInquiryTypePage:
    """Page object for contact form inquiry type."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0048ContactFormInquiryTypeLocators()
        self.locators.page = page

    def navigate_to_contact(self) -> None:
        """Navigate to the contact page."""
        self.page.goto("/contact/")

    def inquiry_type_field_should_be_present(self) -> None:
        """Verify Inquiry Type field is present."""
        expect(self.locators.inquiry_type_field).to_be_attached()

    def field_should_have_multiple_options(self) -> None:
        """Verify field has multiple options."""
        options = self.locators.inquiry_type_field.locator("option")
        count = options.count()
        assert count > 1, "Inquiry Type should have multiple options"
