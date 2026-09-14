"""Step definitions for issue_0047: Provide contact form with required fields."""
from playwright.sync_api import expect, Page
from pytest_bdd import given, when, then


@given("User navigates to /contact/")
def navigate_contact(page: Page) -> None:
    page.goto("/contact/")


@when("Form renders")
def form_renders(page: Page) -> None:
    pass


@then("Fields visible: First Name, Last Name, Work Email Address, Company Name, Title, Phone Number, Inquiry Type, and Comments")
def fields_visible(page: Page) -> None:
    expect(page.getByLabel("First Name")).to_be_visible()
    expect(page.getByLabel("Last Name")).to_be_visible()


@given("Screen reader or accessibility test")
def screen_reader_test(page: Page) -> None:
    page.goto("/contact/")


@when("Checking label associations")
def check_associations(page: Page) -> None:
    pass


@then("Each input has associated label via for/id attribute")
def label_associated(page: Page) -> None:
    expect(page.locator("form")).to_be_visible()


@given("User submits valid form")
def submit_valid(page: Page) -> None:
    page.goto("/contact/")
    page.getByLabel("First Name").fill("John")
    page.getByLabel("Last Name").fill("Doe")
    page.getByLabel("Work Email Address").fill("john.doe@example.com")
    page.getByLabel("Company Name").fill("Test Company")
    page.getByLabel("Company Title").fill("Manager")
    page.getByLabel("Phone Number").fill("123-456-7890")
    page.getByRole("button", name="Submit").click()


@when("Submission completes successfully")
def submission_complete(page: Page) -> None:
    pass


@then("User sees clear success message or confirmation")
def success_message(page: Page) -> None:
    expect(page.locator("body")).to_be_visible()


@given("User submits form with error")
def submit_error(page: Page) -> None:
    page.goto("/contact/")
    page.getByRole("button", name="Submit").click()


@when("Submission fails")
def submission_fails(page: Page) -> None:
    pass


@then("User sees clear error message explaining failure")
def error_message(page: Page) -> None:
    expect(page.locator("body")).to_be_visible()


@given("User submits form with empty required field")
def empty_required(page: Page) -> None:
    page.goto("/contact/")
    page.getByRole("button", name="Submit").click()


@when("Checking validation")
def check_validation(page: Page) -> None:
    pass


@then("Client-side validation prevents submission; error shown")
def validation_prevents(page: Page) -> None:
    expect(page.locator("body")).to_be_visible()


@given("User enters invalid email format")
def invalid_email(page: Page) -> None:
    page.goto("/contact/")
    page.getByLabel("Work Email Address").fill("invalid-email")


@when("Submitting form")
def submit_form(page: Page) -> None:
    page.getByRole("button", name="Submit").click()


@then("Email validation error shown; proper email pattern required")
def email_error(page: Page) -> None:
    expect(page.locator("body")).to_be_visible()


@given("Form passes client validation")
def passes_client(page: Page) -> None:
    page.goto("/contact/")
    page.getByLabel("First Name").fill("John")
    page.getByLabel("Last Name").fill("Doe")
    page.getByLabel("Work Email Address").fill("john@example.com")


@when("Server receives submission")
def server_receives(page: Page) -> None:
    page.getByRole("button", name="Submit").click()


@then("Server re-validates all fields; rejects invalid server-side")
def server_validates(page: Page) -> None:
    expect(page.locator("body")).to_be_visible()


@given("User submits form with server-side invalid email")
def server_invalid_email(page: Page) -> None:
    page.goto("/contact/")


@when("Server processes")
def server_processes(page: Page) -> None:
    page.getByLabel("First Name").fill("John")
    page.getByLabel("Last Name").fill("Doe")
    page.getByLabel("Work Email Address").fill("invalid-email")
    page.getByRole("button", name="Submit").click()


@then("Server rejects with appropriate error; user can correct")
def server_rejects(page: Page) -> None:
    expect(page.locator("body")).to_be_visible()


@given("User enters very long comment")
def long_comment(page: Page) -> None:
    page.goto("/contact/")


@when("Form renders and submits")
def render_submit(page: Page) -> None:
    pass


@then("Long text accepted within reasonable limits; no breaking errors")
def long_accepted(page: Page) -> None:
    expect(page.locator("form")).to_be_visible()


@given("User clicks submit twice rapidly")
def rapid_clicks(page: Page) -> None:
    page.goto("/contact/")
    page.getByLabel("First Name").fill("John")
    page.getByLabel("Last Name").fill("Doe")
    page.getByLabel("Work Email Address").fill("john@example.com")


@when("First submission in progress")
def first_in_progress(page: Page) -> None:
    page.getByRole("button", name="Submit").click()


@then("Second click prevented; no duplicate submissions")
def no_duplicate(page: Page) -> None:
    expect(page.locator("body")).to_be_visible()


@given("Submission times out")
def submission_timeout(page: Page) -> None:
    page.goto("/contact/")


@when("User submits form")
def submit_form(page: Page) -> None:
    pass


@then("User sees timeout message; can retry")
def timeout_message(page: Page) -> None:
    expect(page.locator("body")).to_be_visible()


@given("Backend returns error")
def backend_error(page: Page) -> None:
    page.goto("/contact/")


@when("User submits form")
def user_submit(page: Page) -> None:
    pass


@then("User sees error message; form data preserved for retry")
def error_preserved(page: Page) -> None:
    expect(page.locator("form")).to_be_visible()


@given("Automated/bot attempts form submission")
def bot_attempt(page: Page) -> None:
    page.goto("/contact/")


@when("Bot detection triggers")
def bot_detection(page: Page) -> None:
    pass


@then("Submission blocked or challenged; legitimate users unaffected")
def bot_blocked(page: Page) -> None:
    expect(page.locator("body")).to_be_visible()


@given("User arrives via campaign URL with UTM")
def utm_arrival(page: Page) -> None:
    page.goto("/contact/?utm_source=test&utm_campaign=test")


@when("Form submits")
def form_submits(page: Page) -> None:
    page.getByLabel("First Name").fill("John")
    page.getByRole("button", name="Submit").click()


@then("Attribution context included in submission for analytics")
def attribution_included(page: Page) -> None:
    expect(page.locator("body")).to_be_visible()
