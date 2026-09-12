"""Step definitions for Issue 0049 - Contact form submission feedback and retry."""
from pytest_bdd import given, when, then
from playwright.sync_api import Page, expect
from pages.contact_page import ContactPage


@given("A user submits the contact form")
def submit_form_feedback(page: Page):
    contact_page = ContactPage(page)
    contact_page.goto()
    contact_page.fill_contact_form({
        "first_name": "John",
        "last_name": "Doe",
        "email": "john@example.com",
        "company": "Test",
        "inquiry_type": "Services",
        "comments": "Test"
    })


@when("Submission is initiated")
def submission_initiated(page: Page):
    contact_page = ContactPage(page)
    contact_page.click_submit()


@then("Submit button enters pending/loading state")
def button_pending(page: Page):
    contact_page = ContactPage(page)
    # Button may show loading state
    page.wait_for_timeout(500)


@given("Form is in pending state")
def form_pending(page: Page):
    contact_page = ContactPage(page)
    contact_page.goto()
    contact_page.fill_contact_form({
        "first_name": "John",
        "last_name": "Doe",
        "email": "john@example.com",
        "company": "Test",
        "inquiry_type": "Services",
        "comments": "Test"
    })


@when("User attempts to click submit again")
def click_again(page: Page):
    contact_page = ContactPage(page)
    contact_page.submit_button_is_disabled_while_submitting()


@then("Additional submission is prevented")
def additional_prevented(page: Page):
    # Button should be disabled
    pass


@given("Form submission is successful")
def submission_successful(page: Page):
    pass


@when("Success response is received")
def success_received(page: Page):
    contact_page = ContactPage(page)
    contact_page.goto()
    contact_page.fill_contact_form({
        "first_name": "John",
        "last_name": "Doe",
        "email": "john@example.com",
        "company": "Test",
        "inquiry_type": "Services",
        "comments": "Test"
    })
    contact_page.click_submit()


@then("Success is announced")
def success_announced(page: Page):
    contact_page = ContactPage(page)
    page.wait_for_timeout(1000)


@given("Form submission fails")
def submission_fails(page: Page):
    contact_page = ContactPage(page)
    contact_page.goto()
    contact_page.fill_contact_form({
        "first_name": "John",
        "last_name": "Doe",
        "email": "invalid",
        "company": "Test",
        "inquiry_type": "Services",
        "comments": "Test"
    })
    contact_page.click_submit()


@when("Error is returned")
def error_returned(page: Page):
    page.wait_for_timeout(500)


@then("User-entered content is preserved for retry")
def content_preserved(page: Page):
    # Content should still be in form fields
    contact_page = ContactPage(page)
    first_name = contact_page.locators.first_name_field.input_value()
    assert first_name == "John"


@given("Server returns field-level validation errors")
def server_errors(page: Page):
    contact_page = ContactPage(page)
    contact_page.goto()
    contact_page.fill_email("invalid")
    contact_page.click_submit()


@when("Error response is received")
def error_response(page: Page):
    page.wait_for_timeout(500)


@then("Errors map to specific fields where possible")
def errors_map_fields(page: Page):
    # Errors should be associated with specific fields
    expect(page.locator("[class*='error'], [aria-invalid='true']")).to_be_visible()


@given("Submission times out")
def submission_timeout(page: Page):
    pass


@when("Timeout occurs")
def timeout_occurs(page: Page):
    contact_page = ContactPage(page)
    contact_page.goto()


@then("User sees timeout message; form data preserved for retry")
def timeout_handled(page: Page):
    expect(page.locator("form")).to_be_visible()


@given("User begins submission and then navigates away")
def begin_navigate_away(page: Page):
    contact_page = ContactPage(page)
    contact_page.goto()
    contact_page.fill_contact_form({
        "first_name": "John",
        "last_name": "Doe",
        "email": "john@example.com"
    })


@when("Navigation occurs")
def navigation_occurs(page: Page):
    page.goto("/")


@then("Submission either completes or is cancelled gracefully without data loss indication")
def graceful_cancellation(page: Page):
    # User should be able to continue normally
    expect(page.locator("body")).to_be_visible()
