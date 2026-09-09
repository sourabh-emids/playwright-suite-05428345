"""Step definitions for issue_0005 contact form validation."""

from playwright.sync_api import Page
from pytest_bdd import given, then, when

from pages.issue_0005_contact_validation_page import ContactValidationPage


@given(
    "the contact form is open with every required field empty",
    target_fixture="contact_page",
)
def open_empty_contact_form(page: Page) -> ContactValidationPage:
    contact_page = ContactValidationPage(page)
    contact_page.open()
    return contact_page


@when("the user submits the empty contact form")
def submit_empty_contact_form(
    contact_page: ContactValidationPage,
) -> None:
    contact_page.submit_empty_form()


@then("each required field provides a clear validation message")
def verify_required_messages(
    contact_page: ContactValidationPage,
) -> None:
    contact_page.assert_all_required_messages()


@then("the contact form is not submitted")
def verify_form_not_submitted(
    contact_page: ContactValidationPage,
) -> None:
    contact_page.assert_form_was_not_submitted()
