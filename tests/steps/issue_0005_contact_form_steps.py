from playwright.sync_api import Page
from pytest_bdd import given, then, when

from pages.issue_0005_contact_form_page import Issue0005ContactFormPage


@given(
    "the contact form is open with every required field empty",
    target_fixture="contact_form_page",
)
def empty_contact_form(page: Page) -> Issue0005ContactFormPage:
    contact_form_page = Issue0005ContactFormPage(page)
    contact_form_page.open_with_empty_required_fields()
    return contact_form_page


@when("the user attempts to submit the contact form")
def submit_empty_form(contact_form_page: Issue0005ContactFormPage) -> None:
    contact_form_page.submit()


@then("the contact form submission is prevented")
def verify_submission_prevented(
    contact_form_page: Issue0005ContactFormPage,
) -> None:
    contact_form_page.assert_submission_prevented()


@then("clear validation feedback appears for every required field")
def verify_required_feedback(
    contact_form_page: Issue0005ContactFormPage,
) -> None:
    contact_form_page.assert_every_required_field_has_feedback()
