"""Step bindings for TC-05 contact-form validation."""

import pytest
from playwright.sync_api import Page
from pytest_bdd import given, then, when

from pages.tc_05_contact_validation_page import ContactValidationPage


@pytest.fixture
def contact_form(page: Page) -> ContactValidationPage:
    return ContactValidationPage(page)


@given("the contact form is open with all required fields empty")
def open_empty_form(contact_form: ContactValidationPage) -> None:
    contact_form.open_empty_form()


@when("the empty contact form is submitted")
def submit_empty_form(contact_form: ContactValidationPage) -> None:
    contact_form.submit()


@then("every empty required field shows a clear validation message")
def verify_required_messages(contact_form: ContactValidationPage) -> None:
    contact_form.assert_every_required_field_is_validated()


@then("the incomplete contact form is not submitted")
def verify_form_not_submitted(contact_form: ContactValidationPage) -> None:
    contact_form.assert_form_remains_open()
