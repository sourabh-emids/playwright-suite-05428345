"""Page object for Contact form - EMIDS-LP-047, EMIDS-LP-048, EMIDS-LP-049"""
from playwright.sync_api import Page, expect
from locators.EMIDS-LP-047_contact_form_locators import ContactFormLocators


class ContactFormPage:
    """Page object for Contact form functionality."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = ContactFormLocators(page)

    def goto(self, path: str = "/contact/") -> None:
        self.page.goto(path)

    def verify_form_visible(self) -> None:
        expect(self.locators.form).to_be_visible()

    def verify_required_fields(self) -> None:
        expect(self.locators.first_name_field).to_be_visible()
        expect(self.locators.last_name_field).to_be_visible()
        expect(self.locators.email_field).to_be_visible()
        expect(self.locators.company_field).to_be_visible()
        expect(self.locators.title_field).to_be_visible()
        expect(self.locators.phone_field).to_be_visible()
        expect(self.locators.inquiry_type_field).to_be_visible()
        expect(self.locators.comments_field).to_be_visible()

    def fill_form(self, data: dict) -> None:
        if "first_name" in data:
            self.locators.first_name_field.fill(data["first_name"])
        if "last_name" in data:
            self.locators.last_name_field.fill(data["last_name"])
        if "email" in data:
            self.locators.email_field.fill(data["email"])
        if "company" in data:
            self.locators.company_field.fill(data["company"])
        if "title" in data:
            self.locators.title_field.fill(data["title"])
        if "phone" in data:
            self.locators.phone_field.fill(data["phone"])
        if "inquiry_type" in data:
            self.locators.inquiry_type_field.select_option(data["inquiry_type"])
        if "comments" in data:
            self.locators.comments_field.fill(data["comments"])

    def submit_form(self) -> None:
        self.locators.submit_button.click()

    def select_inquiry_type(self, value: str) -> None:
        self.locators.inquiry_type_field.select_option(value)

    def get_inquiry_options(self) -> list[str]:
        return self.locators.inquiry_type_field.locator("option").all_text_contents()

    def verify_success_message(self) -> None:
        expect(self.locators.success_message).to_be_visible()

    def verify_error_message(self) -> None:
        expect(self.locators.error_message.first).to_be_visible()

    def fill_with_invalid_email(self) -> None:
        self.locators.email_field.fill("invalid-email")
        self.submit_form()

    def verify_email_error(self) -> None:
        expect(self.locators.email_field).to_have_attribute("aria-invalid", "true")
