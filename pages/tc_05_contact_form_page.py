"""Page object for TC-05 contact-form validation."""

import re

from playwright.sync_api import expect

from locators.tc_05_contact_form_locators import (
    CONTACT_FORM,
    CONTACT_PATH,
    INVALID_REQUIRED_FIELDS,
    REQUIRED_FIELDS,
    SUBMIT_BUTTON,
    VALIDATION_MESSAGE,
)
from pages.base_page import BasePage


class ContactFormPage(BasePage):
    """Interactions with the public contact form."""

    def load(self) -> None:
        self.goto(CONTACT_PATH)
        self.dismiss_cookie_banner()
        expect(self.page.locator(CONTACT_FORM)).to_be_visible()

    def submit_empty_form(self) -> None:
        self.page.locator(SUBMIT_BUTTON).click()

    def assert_required_fields_invalid(self) -> None:
        for selector in REQUIRED_FIELDS:
            field = self.page.locator(selector)
            expect(field).to_have_class(re.compile(r"\bmktoInvalid\b"))
            expect(field).to_have_attribute("aria-required", "true")
        expect(self.page.locator(INVALID_REQUIRED_FIELDS)).to_have_count(
            len(REQUIRED_FIELDS)
        )
        expect(self.page.locator(VALIDATION_MESSAGE).first).to_contain_text(
            "This field is required."
        )
        expect(self.page.locator(SUBMIT_BUTTON)).to_be_visible()
