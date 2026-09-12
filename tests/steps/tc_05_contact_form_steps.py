"""Step definitions for TC-05."""

from playwright.sync_api import Page
from pytest_bdd import given, then, when

from pages.tc_05_contact_form_page import ContactFormPage


@given("the contact form is open with empty required fields")
def contact_form_is_open(page: Page) -> None:
    ContactFormPage(page).load()


@when("the visitor submits the contact form")
def visitor_submits_contact_form(page: Page) -> None:
    ContactFormPage(page).submit_empty_form()


@then("every required contact field is marked invalid")
def required_contact_fields_are_invalid(page: Page) -> None:
    ContactFormPage(page).assert_required_fields_invalid()


@then("a clear required-field validation message is displayed")
def required_field_message_is_displayed(page: Page) -> None:
    ContactFormPage(page).assert_required_fields_invalid()
