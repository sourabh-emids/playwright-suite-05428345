"""Page object for tc_005 - Contact form validation messages."""
from playwright.sync_api import Page, expect, Locator

from locators.tc_005_form_locators import Tc005FormLocators


class Tc005FormPage:
    """Page object for contact form validation."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Tc005FormLocators(page)

    def navigate_to_contact(self) -> None:
        """Navigate to the contact page."""
        self.page.goto("/contact/")

    def dismiss_cookie_banner(self) -> None:
        """Dismiss the cookie consent banner."""
        allow_button = self.page.get_by_role("button", name="Allow all")
        if allow_button.is_visible():
            allow_button.click()

    def click_submit(self) -> None:
        """Click the submit button."""
        self.locators.submit_button.click()

    def fill_field(self, field: Locator, value: str) -> None:
        """Fill a form field."""
        field.fill(value)

    def clear_field(self, field: Locator) -> None:
        """Clear a form field."""
        field.clear()

    def get_field_value(self, field: Locator) -> str:
        """Get the value of a field."""
        return field.input_value()

    def verify_validation_error_visible(self, error_locator: Locator) -> None:
        """Verify a validation error is visible."""
        expect(error_locator).to_be_visible()

    def verify_no_validation_error(self, error_locator: Locator) -> None:
        """Verify no validation error is visible."""
        expect(error_locator).not_to_be_visible()

    def wait_for_validation(self) -> None:
        """Wait for validation to complete."""
        self.page.wait_for_load_state("networkidle")

    def verify_field_required_indicator(self, field: Locator) -> None:
        """Verify field has required indicator."""
        expect(field).to_have_attribute("required", timeout=5000) or expect(
            field.locator("..").get_by_text("*")
        ).to_be_visible()

    def get_character_count_text(self) -> str:
        """Get character count text."""
        return self.locators.character_count.inner_text()

    def get_validation_errors_count(self) -> int:
        """Get count of visible validation errors."""
        return self.locators.validation_error_messages.count()
