"""Page object for TC-05 required contact-form validation."""
from playwright.sync_api import Page, expect

from locators.tc_05_required_contact_form_validation_locators import (
    Tc05RequiredContactFormValidationLocators,
)
from pages.base_page import BasePage


class Tc05RequiredContactFormValidationPage(BasePage):
    """Models required-field validation implemented by the embedded Marketo form."""

    _VALID_VALUES = {
        "FirstName": "Taylor",
        "LastName": "Tester",
        "Email": "taylor.tester@example.test",
        "Company": "Example Health",
        "Title": "QA Engineer",
        "Phone": "6155550123",
        "mkto71_Inquiry_Type__c": "Services",
        "MktoPersonNotes": "Valid test message.",
    }

    def __init__(self, page: Page):
        super().__init__(page)

    def open(self) -> None:
        response = self.page.goto("/contact/", wait_until="domcontentloaded")
        assert response is not None and response.ok, "Contact page did not load successfully."
        self.dismiss_cookie_consent_if_present()
        expect(
            self.page.locator(Tc05RequiredContactFormValidationLocators.FORM)
        ).to_be_visible()

    def attempt_empty_submission(self) -> None:
        """Attempt the required-fields-empty submission without sending data."""
        self.page.locator(Tc05RequiredContactFormValidationLocators.SUBMIT).click()

    def assert_empty_submission_is_blocked(self) -> None:
        """Verify every required field by making it the first remaining blank value.

        The inspected Marketo implementation presents one blocking error at a
        time. Progressively completing preceding fields verifies validation for
        all required controls without sending a real contact request.
        """
        initial_url = self.page.url
        for index, field_id in enumerate(
            Tc05RequiredContactFormValidationLocators.REQUIRED_FIELD_IDS
        ):
            if index:
                self.page.locator(
                    Tc05RequiredContactFormValidationLocators.SUBMIT
                ).click()
            error = self.page.locator(
                Tc05RequiredContactFormValidationLocators.ERROR_FOR_FIELD.format(
                    field_id=field_id
                )
            )
            expect(error).to_be_visible()
            expect(error).to_have_text("This field is required.")
            assert self.page.url == initial_url, "The incomplete form was submitted."
            self._fill_field(field_id)

    def _fill_field(self, field_id: str) -> None:
        field = self.page.locator(f"#{field_id}")
        if field_id == "mkto71_Inquiry_Type__c":
            field.select_option(self._VALID_VALUES[field_id])
        else:
            field.fill(self._VALID_VALUES[field_id])
