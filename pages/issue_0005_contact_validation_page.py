"""Page object for contact-form required-field validation."""

import re

from playwright.sync_api import expect

from locators.issue_0005_contact_validation_locators import (
    ContactValidationLocators,
)
from pages.issue_0001_website_homepage_page import WebsiteHomepagePage


class ContactValidationPage(WebsiteHomepagePage):
    def open_contact_form(self) -> None:
        self.open("/contact/")
        expect(
            self.page.get_by_role(
                "heading",
                name=ContactValidationLocators.FORM_HEADING_NAME,
                exact=True,
            )
        ).to_be_visible()

    def submit_empty_form(self) -> None:
        self.page.get_by_role(
            "button",
            name=ContactValidationLocators.SUBMIT_NAME,
            exact=True,
        ).click()

    def verify_required_field_validation(self) -> None:
        for selector in ContactValidationLocators.REQUIRED_FIELDS:
            expect(self.page.locator(selector)).to_have_attribute(
                "aria-required",
                "true",
            )

        expect(
            self.page.locator(
                ContactValidationLocators.INVALID_REQUIRED_FIELDS
            )
        ).to_have_count(len(ContactValidationLocators.REQUIRED_FIELDS))
        expect(
            self.page.locator(ContactValidationLocators.FIRST_NAME_ERROR)
        ).to_have_text("This field is required.")

    def verify_form_remains_open(self) -> None:
        expect(
            self.page.get_by_role(
                "button",
                name=ContactValidationLocators.SUBMIT_NAME,
                exact=True,
            )
        ).to_be_visible()
        expect(self.page).to_have_url(re.compile(r".*/contact/?$"))
