"""Step definitions for issue_0048 - Contact form Inquiry Type values."""
from pytest_bdd import given, then, when

from pages.issue_0048_contact_form_inquiry_type_page import Issue0048ContactFormInquiryTypePage


@given("I navigate to the contact page")
def navigate_to_contact(page: Issue0048ContactFormInquiryTypePage):
    """Navigate to the contact page."""
    page.navigate_to_contact()


@when("I view the contact form")
def view_contact_form(page: Issue0048ContactFormInquiryTypePage):
    """View the contact form."""
    pass


@then("the Inquiry Type field should be present")
def inquiry_type_present(page: Issue0048ContactFormInquiryTypePage):
    """Verify Inquiry Type field is present."""
    page.inquiry_type_field_should_be_present()


@then("the field should have multiple options")
def field_has_options(page: Issue0048ContactFormInquiryTypePage):
    """Verify field has multiple options."""
    page.field_should_have_multiple_options()
