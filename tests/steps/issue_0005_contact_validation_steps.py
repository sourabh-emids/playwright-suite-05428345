"""Step bindings for issue_0005 contact-form validation."""

from playwright.sync_api import Page
from pytest_bdd import given, then, when

from pages.issue_0005_contact_validation_page import ContactValidationPage


@given(
    "the contact form is open with all required fields empty",
    target_fixture="contact_validation_page",
)
def open_contact_form(page: Page) -> ContactValidationPage:
    contact_page = ContactValidationPage(page)
    contact_page.open_contact_form()
    return contact_page


@when("the user submits the empty contact form")
def submit_empty_form(
    contact_validation_page: ContactValidationPage,
) -> None:
    contact_validation_page.submit_empty_form()


@then("all required fields are marked invalid with a clear message")
def verify_required_validation(
    contact_validation_page: ContactValidationPage,
) -> None:
    contact_validation_page.verify_required_field_validation()


@then("the contact form remains open without a successful submission")
def verify_form_not_submitted(
    contact_validation_page: ContactValidationPage,
) -> None:
    contact_validation_page.verify_form_remains_open()
