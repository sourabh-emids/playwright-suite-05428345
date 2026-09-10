import re

from playwright.sync_api import Page, expect

from locators.issue_0005_contact_form_locators import (
    Issue0005ContactFormLocators,
)
from pages.base_page import BasePage


class Issue0005ContactFormPage(BasePage):
    @property
    def form(self):
        return self.page.locator(Issue0005ContactFormLocators.FORM)

    @property
    def required_fields(self):
        return [
            self.form.locator(selector)
            for selector in Issue0005ContactFormLocators.REQUIRED_FIELDS
        ]

    @property
    def validation_errors(self):
        return self.form.locator(
            Issue0005ContactFormLocators.VALIDATION_ERROR
        )

    def open_with_empty_required_fields(self) -> None:
        self.page.goto("/contact/")
        self._dismiss_cookie_banner()
        expect(self.form).to_be_visible()
        for field in self.required_fields:
            expect(field).to_have_value("")

    def submit(self) -> None:
        self.form.get_by_role(
            "button",
            name=Issue0005ContactFormLocators.SUBMIT_BUTTON,
            exact=True,
        ).click()

    def assert_submission_prevented(self) -> None:
        expect(self.page).to_have_url(
            re.compile(r".*/contact/(?:[?#].*)?$")
        )
        expect(self.form).to_be_visible()

    def assert_every_required_field_has_feedback(self) -> None:
        expected_count = len(
            Issue0005ContactFormLocators.REQUIRED_FIELDS
        )
        expect(self.validation_errors).to_have_count(expected_count)
        for index in range(expected_count):
            expect(self.validation_errors.nth(index)).to_have_text(
                Issue0005ContactFormLocators.REQUIRED_MESSAGE
            )

    def _dismiss_cookie_banner(self) -> None:
        allow_button = self.page.get_by_role(
            "button",
            name=Issue0005ContactFormLocators.COOKIE_ALLOW_BUTTON,
            exact=True,
        )
        if allow_button.is_visible():
            allow_button.click()
