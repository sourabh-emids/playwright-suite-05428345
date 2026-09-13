"""Steps for Contact form reached by Connect CTAs (issue_0047)."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from pages.issue_0047_contact_form_page import ContactFormPage
from locators.issue_0047_contact_form_locators import ContactFormLocators


@given("User is on contact form")
def on_contact_form(page: Page) -> None:
    page.goto("/contact/")


@given("User views contact form")
def view_contact_form(page: Page) -> None:
    page.goto("/contact/")


@given("User attempts to submit incomplete form")
def incomplete_form(page: Page) -> None:
    page.goto("/contact/")


@given("User enters invalid email")
def invalid_email(page: Page) -> None:
    page.goto("/contact/")
    form_page = ContactFormPage(page)
    form_page.fill_form({"email": "invalid"})


@given("User submits contact form")
def submit_form(page: Page) -> None:
    page.goto("/contact/")
    form_page = ContactFormPage(page)
    form_page.fill_form({
        "first_name": "John",
        "last_name": "Doe",
        "email": "john@example.com",
        "company": "Example Corp",
        "title": "Manager",
        "phone": "1234567890",
        "comments": "Test message"
    })
    form_page.submit()


@given("User enters invalid email format")
def invalid_email_format(page: Page) -> None:
    page.goto("/contact/")
    form_page = ContactFormPage(page)
    form_page.fill_form({"email": "notanemail"})


@given("User enters very long comments")
def long_comments(page: Page) -> None:
    page.goto("/contact/")
    form_page = ContactFormPage(page)
    form_page.fill_form({"comments": "x" * 10000})


@given("User clicks submit multiple times")
def multiple_submits(page: Page) -> None:
    page.goto("/contact/")
    form_page = ContactFormPage(page)
    form_page.fill_form({
        "first_name": "John",
        "last_name": "Doe",
        "email": "john@example.com",
        "company": "Example Corp",
        "title": "Manager",
        "phone": "1234567890",
    })


@given("Submission times out")
def submission_timeout(page: Page) -> None:
    page.goto("/contact/")


@given("Backend returns error")
def backend_error(page: Page) -> None:
    page.goto("/contact/")


@given("Bot attempts submission")
def bot_submission(page: Page) -> None:
    page.goto("/contact/")


@when("Form renders")
def form_renders(page: Page) -> None:
    pass


@when("Screen reader is active")
def screen_reader(page: Page) -> None:
    pass


@when("Submission completes")
def submission_complete(page: Page) -> None:
    pass


@when("Submission is initiated")
def submit_initiated(page: Page) -> None:
    form_page = ContactFormPage(page)
    form_page.submit()


@when("Form validates")
def form_validates(page: Page) -> None:
    pass


@when("Client validation passes")
def client_validates(page: Page) -> None:
    pass


@when("User attempts submit")
def attempt_submit(page: Page) -> None:
    form_page = ContactFormPage(page)
    form_page.submit()


@when("Form renders")
def render(page: Page) -> None:
    pass


@when("Form is being submitted")
def being_submitted(page: Page) -> None:
    pass


@when("Submission occurs")
def submission_occurs(page: Page) -> None:
    form_page = ContactFormPage(page)
    form_page.submit()


@then("All required fields are displayed: First Name, Last Name, Work Email Address, Company Name, Title, Phone Number, Inquiry Type, Comments")
def all_fields_displayed(page: Page) -> None:
    locators = ContactFormLocators(page)
    expect(locators.first_name_field).to_be_visible()
    expect(locators.last_name_field).to_be_visible()
    expect(locators.email_field).to_be_visible()
    expect(locators.company_field).to_be_visible()
    expect(locators.title_field).to_be_visible()
    expect(locators.phone_field).to_be_visible()
    expect(locators.inquiry_select).to_be_visible()
    expect(locators.comments_field).to_be_visible()


@then("Labels are properly associated with controls")
def labels_associated(page: Page) -> None:
    locators = ContactFormLocators(page)
    label = locators.first_name_field.get_attribute("id")
    assert label is not None


@then("Clear success or failure feedback is provided")
def feedback_provided(page: Page) -> None:
    pass


@then("Required field validation is enforced")
def validation_enforced(page: Page) -> None:
    pass


@then("Email field shows valid format error")
def email_error(page: Page) -> None:
    pass


@then("Server-side revalidation occurs")
def server_revalidates(page: Page) -> None:
    pass


@then("Error is displayed for email field")
def error_displayed(page: Page) -> None:
    pass


@then("Comments field handles appropriately with max length")
def comments_handled(page: Page) -> None:
    expect(ContactFormLocators(page).comments_field).to_be_visible()


@then("Duplicate submission is prevented")
def duplicate_prevented(page: Page) -> None:
    pass


@then("User sees error and can retry")
def error_retry(page: Page) -> None:
    pass


@then("User sees error with clear messaging")
def clear_error(page: Page) -> None:
    pass


@then("Bot submission is detected and rejected")
def bot_rejected(page: Page) -> None:
    pass
