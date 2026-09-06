"""Contact-form empty-field validation behavior."""

import re

from playwright.sync_api import Page, expect

from locators.tc_05_contact_validation_locators import (
    ContactValidationLocators,
)
from pages.base_page import BasePage


class ContactValidationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = ContactValidationLocators()

    def open_empty_form(self) -> None:
        self.page.goto(self.locators.CONTACT_PATH)
        expect(
            self.page.get_by_role(
                "heading", name=self.locators.FORM_HEADING, level=3
            )
        ).to_be_visible()
        for field_name in self.locators.REQUIRED_FIELDS:
            field = self.page.get_by_label(field_name, exact=False)
            expect(field).to_be_visible()

    def submit(self) -> None:
        self.page.get_by_role(
            "button", name=self.locators.SUBMIT_BUTTON, exact=True
        ).click()

    def assert_every_required_field_is_validated(self) -> None:
        validation_messages = self.page.get_by_role("alert").filter(
            has_text=self.locators.VALIDATION_MESSAGE
        )
        expect(validation_messages).to_have_count(
            len(self.locators.REQUIRED_FIELDS)
        )

    def assert_form_remains_open(self) -> None:
        expect(self.page).to_have_url(
            re.compile(r"/contact/(?:[?#].*)?$")
        )
        expect(
            self.page.get_by_role(
                "heading", name=self.locators.FORM_HEADING, level=3
            )
        ).to_be_visible()
