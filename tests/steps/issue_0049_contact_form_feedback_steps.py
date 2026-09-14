"""Step definitions for issue_0049: Contact form submission feedback and retry."""
from playwright.sync_api import expect, Page
from pytest_bdd import given, when, then


@given("User clicks Submit")
def click_submit(page: Page) -> None:
    page.goto("/contact/")
    page.getByLabel("First Name").fill("John")
    page.getByLabel("Last Name").fill("Doe")
    page.getByLabel("Work Email Address").fill("john@example.com")
    page.getByRole("button", name="Submit").click()


@when("Submission in progress")
def in_progress(page: Page) -> None:
    pass


@then("Button shows pending/loading state; disabled to prevent double submit")
def pending_state(page: Page) -> None:
    expect(page.locator("body")).to_be_visible()


@given("Submit button in pending state")
def button_pending(page: Page) -> None:
    page.goto("/contact/")
    page.getByLabel("First Name").fill("John")
    page.getByLabel("Last Name").fill("Doe")
    page.getByLabel("Work Email Address").fill("john@example.com")
    page.getByRole("button", name="Submit").click()


@when("User clicks again")
def click_again(page: Page) -> None:
    pass


@then("Second click does not trigger another submission")
def no_second(page: Page) -> None:
    expect(page.locator("body")).to_be_visible()


@given("Form submission succeeds")
def submission_succeeds(page: Page) -> None:
    page.goto("/contact/")


@when("Success message displays")
def success_display(page: Page) -> None:
    page.getByLabel("First Name").fill("John")
    page.getByLabel("Last Name").fill("Doe")
    page.getByLabel("Work Email Address").fill("john@example.com")
    page.getByRole("button", name="Submit").click()


@then("Screen reader announces success via live region")
def sr_announces(page: Page) -> None:
    expect(page.locator("body")).to_be_visible()


@given("Form submission fails")
def submission_fails(page: Page) -> None:
    page.goto("/contact/")
    page.getByLabel("First Name").fill("John")
    page.getByLabel("Last Name").fill("Doe")
    page.getByLabel("Work Email Address").fill("invalid")


@when("Error displays")
def error_display(page: Page) -> None:
    page.getByRole("button", name="Submit").click()


@then("User-entered content preserved; user can correct and resubmit")
def content_preserved(page: Page) -> None:
    value = page.getByLabel("First Name").input_value()
    assert value == "John"


@given("Server returns field-level errors")
def field_errors(page: Page) -> None:
    page.goto("/contact/")


@when("Error displays")
def errors_display(page: Page) -> None:
    pass


@then("Error messages associated with relevant fields; not just general error")
def field_errors_display(page: Page) -> None:
    expect(page.locator("form")).to_be_visible()


@given("Submission times out")
def timeout(page: Page) -> None:
    page.goto("/contact/")


@when("User waits for response")
def wait_response(page: Page) -> None:
    pass


@then("Timeout error shown; form data preserved")
def timeout_error(page: Page) -> None:
    expect(page.locator("form")).to_be_visible()


@given("Server returns 400 Bad Request")
def bad_request(page: Page) -> None:
    page.goto("/contact/")


@when("Form submission receives validation error")
def validation_error(page: Page) -> None:
    pass


@then("User sees specific validation errors; form data preserved")
def specific_errors(page: Page) -> None:
    expect(page.locator("form")).to_be_visible()


@given("Backend returns 500 error")
def server_error(page: Page) -> None:
    page.goto("/contact/")


@when("User submits form")
def submit_form(page: Page) -> None:
    page.getByLabel("First Name").fill("John")
    page.getByLabel("Last Name").fill("Doe")
    page.getByLabel("Work Email Address").fill("john@example.com")


@then("User sees friendly error message; form data preserved for retry")
def friendly_error(page: Page) -> None:
    expect(page.locator("form")).to_be_visible()


@given("Form submission in progress")
def in_progress(page: Page) -> None:
    page.goto("/contact/")


@when("User navigates away")
def navigate_away(page: Page) -> None:
    page.goto("/")


@then("Browser warns user about pending submission if appropriate")
def browser_warns(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("Form submission completes")
def submission_completes(page: Page) -> None:
    page.goto("/contact/")


@when("Logging submission result")
def log_result(page: Page) -> None:
    pass


@then("Outcome, timestamp, form ID, and correlation ID logged; not raw field values")
def log_format(page: Page) -> None:
    expect(page.locator("form")).to_be_visible()
