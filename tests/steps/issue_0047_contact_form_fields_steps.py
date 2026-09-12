"""Step definitions for issue_0047 - Contact form fields and accessibility."""
from pytest_bdd import given, then, when

from pages.issue_0047_contact_form_fields_page import Issue0047ContactFormFieldsPage


@given("I navigate to the contact page")
def navigate_to_contact(page: Issue0047ContactFormFieldsPage):
    """Navigate to the contact page."""
    page.navigate_to_contact()


@when("I view the contact form")
def view_contact_form(page: Issue0047ContactFormFieldsPage):
    """View the contact form."""
    pass


@then("the form fields should have labels")
def form_fields_have_labels(page: Issue0047ContactFormFieldsPage):
    """Verify form fields have labels."""
    page.form_fields_should_have_labels()


@then("the fields should be keyboard accessible")
def fields_keyboard_accessible(page: Issue0047ContactFormFieldsPage):
    """Verify fields are keyboard accessible."""
    page.fields_should_be_keyboard_accessible()
