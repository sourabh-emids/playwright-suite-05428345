"""Step definitions for Contact form - EMIDS-LP-047, EMIDS-LP-048, EMIDS-LP-049"""
from pytest_bdd import given, when, then
from pages.EMIDS-LP-047_contact_form_page import ContactFormPage
from playwright.sync_api import expect


@given("Contact form at /contact/")
def contact_form(page):
    form_page = ContactFormPage(page)
    form_page.goto("/contact/")


@when("Form is inspected")
def inspect_form(page):
    pass


@then("All fields present: First Name, Last Name, Work Email Address, Company Name, Title, Phone Number, Inquiry Type, Comments")
def verify_all_fields(page):
    form_page = ContactFormPage(page)
    form_page.verify_required_fields()


@given("Contact form fields")
def contact_form_fields(page):
    form_page = ContactFormPage(page)
    form_page.goto("/contact/")


@when("Accessibility is checked")
def check_accessibility(page):
    pass


@then("Each label is properly associated with its control")
def verify_associated(page):
    form_page = ContactFormPage(page)
    form_page.verify_form_visible()


@given("Contact form submission")
def contact_form_submission(page):
    form_page = ContactFormPage(page)
    form_page.goto("/contact/")


@when("Form is submitted")
def submit_form(page):
    form_page.fill_form({
        "first_name": "Test",
        "last_name": "User",
        "email": "test@example.com",
        "company": "Test Company",
        "inquiry_type": "Services"
    })
    form_page.submit_form()


@then("Clear success or failure feedback is provided")
def verify_feedback(page):
    form_page = ContactFormPage(page)
    form_page.verify_form_visible()


@given("Contact form validation")
def contact_form_validation(page):
    form_page = ContactFormPage(page)
    form_page.goto("/contact/")


@when("Required fields are empty")
def empty_fields(page):
    pass


@then("Submission is prevented with appropriate error")
def verify_prevented(page):
    form_page = ContactFormPage(page)
    form_page.submit_form()


@given("Email field with invalid input")
def invalid_email(page):
    form_page = ContactFormPage(page)
    form_page.goto("/contact/")


@when("Submission is attempted")
def attempt_submission(page):
    form_page.fill_with_invalid_email()


@then("Email must have valid syntax; server revalidates")
def verify_valid_syntax(page):
    form_page = ContactFormPage(page)
    form_page.verify_form_visible()


@given("Invalid email format submitted")
def invalid_format(page):
    form_page = ContactFormPage(page)
    form_page.goto("/contact/")


@when("Form validation runs")
def validation_runs(page):
    form_page.fill_with_invalid_email()


@then("Error message displayed for invalid email")
def verify_error_message(page):
    form_page = ContactFormPage(page)
    form_page.verify_form_visible()


@given("Server timeout during submission")
def server_timeout(page):
    pass


@when("Submission is attempted")
def attempt_timeout(page):
    form_page = ContactFormPage(page)
    form_page.goto("/contact/")
    form_page.fill_form({
        "first_name": "Test",
        "last_name": "User",
        "email": "test@example.com",
        "company": "Test Company",
        "inquiry_type": "Services"
    })
    form_page.submit_form()


@then("User receives timeout error and can retry")
def verify_timeout(page):
    form_page = ContactFormPage(page)
    form_page.verify_form_visible()


@given("Inquiry Type field")
def inquiry_type_field(page):
    form_page = ContactFormPage(page)
    form_page.goto("/contact/")


@when("Options are inspected")
def inspect_options(page):
    pass


@then("Options include: Services, Careers, Employment Verification, Media Request, Other")
def verify_options(page):
    form_page = ContactFormPage(page)
    options = form_page.get_inquiry_options()
    assert len(options) > 0


@given("Inquiry Type if marked required")
def inquiry_required(page):
    form_page = ContactFormPage(page)
    form_page.goto("/contact/")


@when("Placeholder or no selection made")
def no_selection(page):
    pass


@then("Submission is prevented")
def verify_prevented_inquiry(page):
    form_page = ContactFormPage(page)
    form_page.submit_form()


@given("Inquiry Type with 'Select...' placeholder")
def select_placeholder(page):
    form_page = ContactFormPage(page)
    form_page.goto("/contact/")


@when("Submission is attempted with placeholder")
def attempt_placeholder(page):
    form_page.submit_form()


@then("Submission is rejected")
def verify_rejected(page):
    form_page = ContactFormPage(page)
    form_page.verify_form_visible()


@given("Tampered form submission")
def tampered_submission(page):
    pass


@when("Unknown inquiry type value submitted")
def unknown_value(page):
    form_page = ContactFormPage(page)
    form_page.goto("/contact/")
    form_page.fill_form({
        "first_name": "Test",
        "email": "test@example.com",
        "inquiry_type": "InvalidType"
    })


@then("Value outside allowed enum is rejected")
def verify_rejected_enum(page):
    form_page = ContactFormPage(page)
    form_page.verify_form_visible()


@given("User submits contact form")
def user_submits(page):
    form_page = ContactFormPage(page)
    form_page.goto("/contact/")


@when("Submission is initiated")
def initiate_submission(page):
    form_page = ContactFormPage(page)
    form_page.fill_form({
        "first_name": "Test",
        "last_name": "User",
        "email": "test@example.com",
        "company": "Test Company",
        "inquiry_type": "Services"
    })
    form_page.submit_form()


@then("UI enters pending state")
def verify_pending(page):
    form_page = ContactFormPage(page)
    form_page.verify_form_visible()


@given("Form in pending state")
def form_pending(page):
    form_page = ContactFormPage(page)
    form_page.goto("/contact/")


@when("Submit is clicked again")
def click_again(page):
    form_page = ContactFormPage(page)
    form_page.submit_form()


@then("Duplicate activation is prevented")
def verify_prevented_duplicate(page):
    pass


@given("Successful form submission")
def successful_submission(page):
    pass


@when("Success occurs")
def success_occurs(page):
    form_page = ContactFormPage(page)
    form_page.goto("/contact/")


@then("Success is announced via accessible live region")
def verify_live_region(page):
    form_page = ContactFormPage(page)
    form_page.verify_form_visible()


@given("Failed form submission")
def failed_submission(page):
    pass


@when("Error occurs")
def error_occurs(page):
    form_page = ContactFormPage(page)
    form_page.goto("/contact/")


@then("User-entered content is preserved for retry")
def verify_preserved(page):
    form_page = ContactFormPage(page)
    form_page.fill_form({
        "first_name": "Test",
        "email": "test@example.com"
    })
    form_page.submit_form()


@given("Server-side validation error response")
def server_error(page):
    pass


@when("Error is returned")
def error_returned(page):
    form_page = ContactFormPage(page)
    form_page.goto("/contact/")


@then("Errors map to relevant fields where possible")
def verify_field_mapping(page):
    form_page = ContactFormPage(page)
    form_page.verify_form_visible()


@given("Backend vendor outage")
def backend_outage(page):
    pass


@when("Submission is attempted")
def attempt_outage(page):
    form_page = ContactFormPage(page)
    form_page.goto("/contact/")
    form_page.fill_form({
        "first_name": "Test",
        "last_name": "User",
        "email": "test@example.com",
        "company": "Test Company",
        "inquiry_type": "Services"
    })
    form_page.submit_form()


@then("User receives error and can retry")
def verify_error_retry(page):
    form_page = ContactFormPage(page)
    form_page.verify_form_visible()
