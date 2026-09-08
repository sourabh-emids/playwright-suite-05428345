import re

from playwright.sync_api import Page, expect

from locators.tc_05_contact_validation_locators import (
    Tc05ContactValidationLocators,
)
from pages.base_page import BasePage


class Tc05ContactValidationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = Tc05ContactValidationLocators

    def open(self) -> None:
        self.goto("/contact/")
        self._dismiss_cookie_banner()
        expect(self.page.locator(self.locators.FORM)).to_be_visible()

    def assert_required_fields_empty(self) -> None:
        form = self.page.locator(self.locators.FORM)
        expect(form.locator(self.locators.REQUIRED)).to_have_count(
            len(self.locators.REQUIRED_FIELDS)
        )
        for selector, _ in self.locators.REQUIRED_FIELDS:
            expect(form.locator(selector)).to_have_value("")

    def submit(self) -> None:
        self.page.locator(self.locators.FORM).get_by_role(
            "button",
            name=self.locators.SUBMIT_NAME,
            exact=True,
        ).click()

    def assert_submission_rejected(self) -> None:
        expect(self.page).to_have_url(
            re.compile(r"^https?://[^/]+/contact/(?:[?#].*)?$")
        )
        expect(self.page.locator(self.locators.FORM)).to_be_visible()

    def assert_required_field_feedback(self) -> None:
        form = self.page.locator(self.locators.FORM)
        expect(form.locator(self.locators.INVALID_REQUIRED)).to_have_count(
            len(self.locators.REQUIRED_FIELDS)
        )

        for selector, message in self.locators.REQUIRED_FIELDS:
            field = form.locator(selector)
            field.click()
            expect(field).to_have_attribute("aria-invalid", "true")
            expect(field).to_have_attribute(
                "aria-describedby",
                re.compile(r"^ValidMsg"),
            )
            expect(form.get_by_role("alert")).to_contain_text(message)

    def _dismiss_cookie_banner(self) -> None:
        allow_all = self.page.get_by_role(
            "button",
            name=self.locators.COOKIE_ALLOW_NAME,
            exact=True,
        )
        if allow_all.count() and allow_all.is_visible():
            allow_all.click()
