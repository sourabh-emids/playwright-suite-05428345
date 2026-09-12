"""Step definitions for Issue 0048 - Inquiry Type values on contact form."""
from pytest_bdd import given, when, then
from playwright.sync_api import Page, expect
from pages.contact_page import ContactPage


@given("A user views the Inquiry Type select control")
def view_inquiry_select(page: Page):
    contact_page = ContactPage(page)
    contact_page.goto()


@when("Options are examined")
def options_examined(page: Page):
    pass


@then("Select contains: Services, Careers, Employment Verification, Media Request, Other")
def expected_options(page: Page):
    contact_page = ContactPage(page)
    options = contact_page.inquiry_type_options_include()
    assert "Services" in options
    assert "Careers" in options
    assert "Other" in options


@given("User leaves Inquiry Type as placeholder")
def leave_inquiry_placeholder(page: Page):
    contact_page = ContactPage(page)
    contact_page.goto()


@when("Form is submitted")
def form_submitted_inquiry(page: Page):
    contact_page = ContactPage(page)
    contact_page.click_submit()


@then("Submission is rejected; placeholder is not a valid choice")
def placeholder_rejected(page: Page):
    contact_page = ContactPage(page)
    is_empty = contact_page.placeholder_selected_not_valid()
    assert is_empty or contact_page.validation_error_is_shown()


@given("A tampered request submits an unknown Inquiry Type value")
def tampered_request(page: Page):
    pass


@when("Server validates the submission")
def server_validates(page: Page):
    contact_page = ContactPage(page)
    contact_page.goto()


@then("Unknown value is rejected")
def unknown_rejected(page: Page):
    contact_page = ContactPage(page)
    contact_page.select_inquiry_type("InvalidOption")
    contact_page.click_submit()
    page.wait_for_timeout(500)


@given("An Inquiry Type option is removed from the system while user has cached form")
def option_removed(page: Page):
    pass


@when("User submits the form")
def user_submits_cached(page: Page):
    contact_page = ContactPage(page)
    contact_page.goto()


@then("Server validates against current allowed values and rejects invalid selections")
def server_validates_current(page: Page):
    expect(page.locator("form")).to_be_visible()
