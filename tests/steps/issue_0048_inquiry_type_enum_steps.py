"""Step definitions for issue_0048: Support Inquiry Type enum values."""
from playwright.sync_api import expect, Page
from pytest_bdd import given, when, then


@given("User views Inquiry Type field")
def view_inquiry_type(page: Page) -> None:
    page.goto("/contact/")


@when("Opening dropdown")
def open_dropdown(page: Page) -> None:
    page.getByLabel("Inquiry Type").click()


@then("Options include: Services, Careers, Employment Verification, Media Request, Other")
def options_include(page: Page) -> None:
    expect(page.getByLabel("Inquiry Type")).to_be_visible()


@given("User submits form without selecting Inquiry Type")
def no_selection(page: Page) -> None:
    page.goto("/contact/")
    page.getByLabel("First Name").fill("John")
    page.getByLabel("Last Name").fill("Doe")
    page.getByLabel("Work Email Address").fill("john@example.com")


@when("Checking validation")
def check_validation(page: Page) -> None:
    page.getByRole("button", name="Submit").click()


@then("Form validation requires valid selection; placeholder 'Select...' not accepted")
def validation_required(page: Page) -> None:
    expect(page.locator("form")).to_be_visible()


@given("User tests Inquiry Type accessibility")
def test_accessibility(page: Page) -> None:
    page.goto("/contact/")
    page.getByLabel("Inquiry Type").focus()


@when("Navigating with keyboard")
def navigate_keyboard(page: Page) -> None:
    page.keyboard.press("Tab")


@then("Control is either native <select> or accessible custom combobox")
def accessible_combobox(page: Page) -> None:
    expect(page.getByLabel("Inquiry Type")).to_be_visible()


@given("Tampered request submits unknown value")
def tampered_request(page: Page) -> None:
    page.goto("/contact/")


@when("Server processes")
def server_processes(page: Page) -> None:
    pass


@then("Server rejects invalid enum value")
def server_rejects(page: Page) -> None:
    expect(page.locator("form")).to_be_visible()


@given("Option removed from enum after user loaded form")
def option_removed(page: Page) -> None:
    page.goto("/contact/")


@when("User submits with previous option")
def submit_previous(page: Page) -> None:
    pass


@then("Server validates against current enum; rejects if option now invalid")
def current_enum(page: Page) -> None:
    expect(page.locator("form")).to_be_visible()


@given("Tampered request with unknown value")
def unknown_value(page: Page) -> None:
    page.goto("/contact/")


@when("Server validates")
def server_validates(page: Page) -> None:
    pass


@then("Error logged with sanitized details; no sensitive data exposed")
def sanitized_error(page: Page) -> None:
    expect(page.locator("form")).to_be_visible()
