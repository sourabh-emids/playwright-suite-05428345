"""Page object for the public Emids contact form."""

from playwright.sync_api import Page, expect

from locators.emids_locators import ContactFormLocators
from pages.emids_site_page import EmidsSitePage


class ContactPage(EmidsSitePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def open(self) -> None:
        self.last_response = self.page.goto("/contact/", wait_until="domcontentloaded")
        self._dismiss_cookie_banner_if_present()
        expect(
            self.page.get_by_role(
                "heading", name=ContactFormLocators.FORM_HEADING, exact=True
            )
        ).to_be_visible()

    def verify_all_required_fields_are_empty(self) -> None:
        for selector in ContactFormLocators.REQUIRED_FIELD_SELECTORS:
            expect(self.page.locator(selector)).to_have_value("")

    def submit_empty_form(self) -> None:
        self.page.get_by_role(
            "button", name=ContactFormLocators.SUBMIT_BUTTON_NAME, exact=True
        ).click()

    def verify_required_field_validation(self) -> None:
        # The Marketo form marks its complete required-field inventory with
        # aria-required. On an empty submit it reports the first invalid field
        # with a live alert, allowing the user to correct fields in sequence.
        for selector in ContactFormLocators.REQUIRED_FIELD_SELECTORS:
            expect(self.page.locator(selector)).to_have_attribute(
                "aria-required", "true"
            )

        first_required_field = self.page.locator(
            ContactFormLocators.REQUIRED_FIELD_SELECTORS[0]
        )
        expect(first_required_field).to_have_attribute("aria-invalid", "true")
        expect(
            self.page.get_by_role("alert").filter(
                has_text=ContactFormLocators.REQUIRED_MESSAGE
            )
        ).to_be_visible()
