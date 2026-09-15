"""Steps for issue_0005: Contact form validates required fields."""
from pytest_bdd import given, when, then

from pages.issue_0005_contact_form_validation_page import ContactFormValidationPage


@given("The contact form page is loaded with all required fields visible")
def contact_form_loaded(page, contact_form_validation_page):
    contact_form_validation_page.load_contact_page()


@when("The user submits the contact form with all required fields left empty")
def submit_empty_form(page, contact_form_validation_page):
    contact_form_validation_page.submit_empty_form()


@then("Clear validation messages appear indicating required fields must be completed")
def verify_validation_messages(page, contact_form_validation_page):
    contact_form_validation_page.verify_validation_messages_appear()
