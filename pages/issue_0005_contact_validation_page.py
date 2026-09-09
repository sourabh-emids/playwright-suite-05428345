"""Page object for required contact form validation."""

import re

from playwright.sync_api import Locator, Page, expect

from locators.issue_0005_contact_validation_locators import (
    ContactValidationLocators,
)
from pages.base_page import BasePage


class ContactValidationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = ContactValidationLocators

    def open(self) -> None:
        self.goto("/contact/")
        self._dismiss_cookie_banner()
        expect(self.form).to_be_visible()
        for selector, _ in self.locators.REQUIRED_FIELDS:
            expect(self.form.locator(selector)).to_have_value("")

    def submit_empty_form(self) -> None:
        self.form.get_by_role(
            "button",
            name=self.locators.SUBMIT,
            exact=True,
        ).click()

    def assert_all_required_messages(self) -> None:
        alert = self.form.get_by_role("alert")
        for selector, message in self.locators.REQUIRED_FIELDS:
            field = self.form.locator(selector)
            field.focus()
            expect(field).to_have_class(re.compile(r"\bmktoInvalid\b"))
            expect(alert).to_have_text(message)

    def assert_form_was_not_submitted(self) -> None:
        expect(self.page).to_have_url(
            re.compile(r".*/contact/(?:[?#].*)?$")
        )
        expect(
            self.page.get_by_role(
                "heading",
                name=self.locators.FORM_HEADING,
                exact=True,
            )
        ).to_be_visible()
        expect(self.form).to_be_visible()

    @property
    def form(self) -> Locator:
        return self.page.locator(self.locators.FORM)

    def _dismiss_cookie_banner(self) -> None:
        allow_all = self.page.get_by_role(
            "button",
            name=self.locators.COOKIE_ALLOW_ALL,
        )
        if allow_all.is_visible():
            allow_all.click()
