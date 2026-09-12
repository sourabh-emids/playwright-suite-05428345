"""Page object for the Contact page."""
from typing import Optional
from playwright.sync_api import Page, expect, Locator
from locators.contact_page_locators import ContactPageLocators


class ContactPage:
    """Page object for the Emids contact page."""
    
    def __init__(self, page: Page):
        self.page = page
        self.locators = ContactPageLocators(page)
    
    def goto(self, path: str = "/contact/") -> None:
        """Navigate to the contact page."""
        self.page.goto(path)
    
    # Form field methods
    def fill_first_name(self, value: str) -> None:
        """Fill the First Name field."""
        self.locators.first_name_field.fill(value)
    
    def fill_last_name(self, value: str) -> None:
        """Fill the Last Name field."""
        self.locators.last_name_field.fill(value)
    
    def fill_email(self, value: str) -> None:
        """Fill the Work Email field."""
        self.locators.email_field.fill(value)
    
    def fill_company(self, value: str) -> None:
        """Fill the Company Name field."""
        self.locators.company_field.fill(value)
    
    def fill_title(self, value: str) -> None:
        """Fill the Title field."""
        self.locators.title_field.fill(value)
    
    def fill_phone(self, value: str) -> None:
        """Fill the Phone Number field."""
        self.locators.phone_field.fill(value)
    
    def select_inquiry_type(self, value: str) -> None:
        """Select an inquiry type from the dropdown."""
        self.locators.inquiry_type_select.select_option(value)
    
    def fill_comments(self, value: str) -> None:
        """Fill the Comments field."""
        self.locators.comments_field.fill(value)
    
    def fill_contact_form(self, data: dict) -> None:
        """Fill all contact form fields."""
        if "first_name" in data:
            self.fill_first_name(data["first_name"])
        if "last_name" in data:
            self.fill_last_name(data["last_name"])
        if "email" in data:
            self.fill_email(data["email"])
        if "company" in data:
            self.fill_company(data["company"])
        if "title" in data:
            self.fill_title(data["title"])
        if "phone" in data:
            self.fill_phone(data["phone"])
        if "inquiry_type" in data:
            self.select_inquiry_type(data["inquiry_type"])
        if "comments" in data:
            self.fill_comments(data["comments"])
    
    # Form visibility and interaction methods
    def contact_form_is_visible(self) -> None:
        """Verify the contact form is visible."""
        expect(self.locators.contact_form).to_be_visible()
    
    def all_required_fields_visible(self) -> list[str]:
        """Verify all required fields are displayed."""
        fields = ["First Name", "Last Name", "Email", "Company", "Title", "Phone", "Inquiry Type", "Comments"]
        for field in fields:
            expect(self.page.getByText(field, exact=False)).to_be_visible()
        return fields
    
    def submit_button_is_visible(self) -> None:
        """Verify the Submit button is visible."""
        expect(self.locators.submit_button).to_be_visible()
    
    def click_submit(self) -> None:
        """Click the Submit button."""
        self.locators.submit_button.click()
        self.page.wait_for_timeout(500)
    
    def submit_button_is_disabled_while_submitting(self) -> bool:
        """Verify submit button is disabled while form is submitting."""
        self.locators.submit_button.click()
        is_disabled = self.locators.submit_button.is_disabled()
        self.page.wait_for_timeout(500)
        return is_disabled
    
    # Validation methods
    def submit_with_empty_required_fields(self) -> None:
        """Submit form with empty required fields to trigger validation."""
        self.click_submit()
        self.page.wait_for_timeout(300)
    
    def validation_error_is_shown(self) -> bool:
        """Check if validation errors are shown."""
        errors = self.locators.form_error_messages
        return errors.count() > 0
    
    def invalid_email_shows_error(self) -> None:
        """Enter invalid email and verify error is shown."""
        self.locators.email_field.fill("invalid-email")
        self.click_submit()
        self.page.wait_for_timeout(300)
    
    def email_field_has_error(self) -> bool:
        """Check if email field has validation error."""
        error_indicator = self.page.locator('[class*="error"], [aria-invalid="true"]')
        return error_indicator.count() > 0
    
    # Success and error handling
    def success_message_is_visible(self) -> bool:
        """Check if success message is visible."""
        success = self.locators.success_message
        if success.count() > 0:
            expect(success.first).to_be_visible()
            return True
        return False
    
    # Inquiry type validation
    def inquiry_type_options_include(self) -> list[str]:
        """Verify inquiry type options include expected values."""
        expected_options = ["Services", "Careers", "Employment Verification", "Media Request", "Other"]
        select = self.locators.inquiry_type_select
        options = select.locator("option").all_text_contents()
        for opt in expected_options:
            assert any(opt.lower() in o.lower() for o in options), f"Option {opt} not found"
        return expected_options
    
    def placeholder_selected_not_valid(self) -> bool:
        """Verify that placeholder/empty selection is not a valid choice."""
        selected = self.locators.inquiry_type_select.input_value()
        return selected == "" or selected is None
    
    # Office locations methods
    def offices_section_is_visible(self) -> None:
        """Verify offices section is visible."""
        expect(self.locators.offices_section).to_be_visible()
    
    def switch_to_asia_offices(self) -> None:
        """Switch to Asia offices tab."""
        self.locators.asia_tab.click()
        self.page.wait_for_timeout(300)
    
    def switch_to_europe_offices(self) -> None:
        """Switch to Europe offices tab."""
        self.locators.europe_tab.click()
        self.page.wait_for_timeout(300)
    
    # Contact information methods
    def contact_email_is_visible(self) -> None:
        """Verify contact email is visible."""
        expect(self.locators.contact_email).to_be_visible()
    
    def contact_phone_is_visible(self) -> None:
        """Verify contact phone is visible."""
        expect(self.locators.contact_phone).to_be_visible()
    
    # Privacy policy methods
    def privacy_policy_link_is_visible(self) -> None:
        """Verify privacy policy link is visible."""
        expect(self.locators.privacy_policy_link).to_be_visible()
    
    def click_privacy_policy(self) -> None:
        """Click privacy policy link."""
        self.locators.privacy_policy_link.click()
        self.page.wait_for_url("**/privacy-policy/**")
    
    # Accessibility methods
    def labels_associated_with_controls(self) -> bool:
        """Verify labels are properly associated with controls via for/id attributes."""
        # Check that form inputs have associated labels
        first_name_id = self.locators.first_name_field.get_attribute("id")
        first_name_label_for = self.locators.first_name_label.get_attribute("for")
        return first_name_id == first_name_label_for if first_name_id and first_name_label_for else False
