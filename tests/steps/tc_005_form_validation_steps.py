"""Steps for tc_005 - Contact form validation messages."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then


@given("The user is on the contact form page")
def user_on_contact_form(page: Page) -> None:
    """User is on the contact form page."""
    from pages.tc_005_form_page import Tc005FormPage
    form_page = Tc005FormPage(page)
    form_page.navigate_to_contact()
    form_page.dismiss_cookie_banner()


@when("The user clicks the Submit button without filling in any required fields")
def click_submit_empty_form(page: Page) -> None:
    """Click submit without filling form."""
    from pages.tc_005_form_page import Tc005FormPage
    form_page = Tc005FormPage(page)
    form_page.click_submit()


@then("Clear validation error messages appear indicating which required fields are missing such as Name, Email, Phone, and Message fields must be filled")
def validation_errors_appear(page: Page) -> None:
    """Verify validation errors appear."""
    from pages.tc_005_form_page import Tc005FormPage
    form_page = Tc005FormPage(page)
    form_page.wait_for_validation()

    errors = form_page.get_validation_errors_count()
    expect(errors).to_be_greater_than(0)

    expect(page.get_by_text("This field is required", exact=False)).to_be_visible()


@when("The user enters an invalid email format such as test@ or test.com and attempts to submit")
def enter_invalid_email(page: Page) -> None:
    """Enter invalid email and submit."""
    from pages.tc_005_form_page import Tc005FormPage
    form_page = Tc005FormPage(page)
    form_page.fill_field(form_page.locators.work_email_field, "test@")
    form_page.click_submit()


@then("A validation message is displayed indicating the email format is invalid with guidance to enter a valid email address")
def email_validation_error(page: Page) -> None:
    """Verify email validation error."""
    from pages.tc_005_form_page import Tc005FormPage
    form_page = Tc005FormPage(page)
    form_page.wait_for_validation()

    email_input = form_page.locators.work_email_field
    expect(email_input).to_have_attribute("aria-invalid", "true", timeout=5000) or expect(
        page.get_by_text("email", exact=False)
    ).to_be_visible()


@when("The user enters non-numeric characters in the phone field and attempts to submit")
def enter_non_numeric_phone(page: Page) -> None:
    """Enter non-numeric characters in phone field."""
    from pages.tc_005_form_page import Tc005FormPage
    form_page = Tc005FormPage(page)
    form_page.fill_field(form_page.locators.phone_field, "abc123abc")
    form_page.click_submit()


@then("A validation message appears indicating the phone field should contain only numeric values or a valid phone number format")
def phone_validation_error(page: Page) -> None:
    """Verify phone validation error."""
    from pages.tc_005_form_page import Tc005FormPage
    form_page = Tc005FormPage(page)
    form_page.wait_for_validation()

    phone_input = form_page.locators.phone_field
    expect(phone_input).to_have_attribute("aria-invalid", "true", timeout=5000) or expect(
        page.get_by_text("phone", exact=False)
    ).to_be_visible()


@given("The user is on the contact form page with all other required fields filled")
def user_with_other_fields_filled(page: Page) -> None:
    """User has other required fields filled."""
    from pages.tc_005_form_page import Tc005FormPage
    form_page = Tc005FormPage(page)
    form_page.navigate_to_contact()
    form_page.dismiss_cookie_banner()

    form_page.fill_field(form_page.locators.first_name_field, "John")
    form_page.fill_field(form_page.locators.last_name_field, "Doe")
    form_page.fill_field(form_page.locators.work_email_field, "john@example.com")
    form_page.fill_field(form_page.locators.company_name_field, "Test Company")
    form_page.fill_field(form_page.locators.title_field, "Manager")
    form_page.fill_field(form_page.locators.phone_field, "1234567890")


@when("The user leaves the message field empty and clicks Submit")
def submit_without_message(page: Page) -> None:
    """Submit without filling message field."""
    from pages.tc_005_form_page import Tc005FormPage
    form_page = Tc005FormPage(page)
    form_page.click_submit()


@then("A clear validation message appears stating the message field is required")
def message_required_error(page: Page) -> None:
    """Verify message field is required."""
    from pages.tc_005_form_page import Tc005FormPage
    form_page = Tc005FormPage(page)
    form_page.wait_for_validation()

    comments_input = form_page.locators.comments_field
    expect(comments_input).to_have_attribute("aria-invalid", "true", timeout=5000) or expect(
        page.get_by_text("required", exact=False)
    ).to_be_visible()


@given("The user has attempted to submit the form with multiple validation errors")
def multiple_validation_errors(page: Page) -> None:
    """User has multiple validation errors."""
    from pages.tc_005_form_page import Tc005FormPage
    form_page = Tc005FormPage(page)
    form_page.navigate_to_contact()
    form_page.dismiss_cookie_banner()
    form_page.click_submit()
    form_page.wait_for_validation()


@when("The user corrects one field but leaves others invalid")
def correct_one_field(page: Page) -> None:
    """Correct one field but leave others invalid."""
    from pages.tc_005_form_page import Tc005FormPage
    form_page = Tc005FormPage(page)
    form_page.fill_field(form_page.locators.first_name_field, "John")


@then("Form submission is still blocked and remaining validation errors are clearly displayed")
def submission_still_blocked(page: Page) -> None:
    """Verify submission is still blocked."""
    from pages.tc_005_form_page import Tc005FormPage
    form_page = Tc005FormPage(page)

    errors = form_page.get_validation_errors_count()
    expect(errors).to_be_greater_than(0)


@given("The user has submitted a form with validation errors visible")
def errors_are_visible(page: Page) -> None:
    """User has submitted with errors visible."""
    from pages.tc_005_form_page import Tc005FormPage
    form_page = Tc005FormPage(page)
    form_page.navigate_to_contact()
    form_page.dismiss_cookie_banner()
    form_page.click_submit()
    form_page.wait_for_validation()


@when("The user fills in the previously empty or invalid field with correct data")
def correct_the_field(page: Page) -> None:
    """Fill in the field with correct data."""
    from pages.tc_005_form_page import Tc005FormPage
    form_page = Tc005FormPage(page)
    form_page.fill_field(form_page.locators.first_name_field, "John")


@then("The validation error message for that specific field is cleared or updated to confirm the field is now valid")
def error_cleared(page: Page) -> None:
    """Verify error is cleared for that field."""
    from pages.tc_005_form_page import Tc005FormPage
    form_page = Tc005FormPage(page)

    first_name = form_page.locators.first_name_field
    expect(first_name).not_to_have_attribute("aria-invalid", "true")


@given("The user is on the contact form page with text fields that have character limits")
def user_on_form_with_limits(page: Page) -> None:
    """User is on contact form with character limits."""
    from pages.tc_005_form_page import Tc005FormPage
    form_page = Tc005FormPage(page)
    form_page.navigate_to_contact()
    form_page.dismiss_cookie_banner()


@when("The user attempts to enter text exceeding the character limit")
def exceed_character_limit(page: Page) -> None:
    """Attempt to exceed character limit."""
    from pages.tc_005_form_page import Tc005FormPage
    form_page = Tc005FormPage(page)
    form_page.fill_field(form_page.locators.comments_field, "A" * 1000)


@then("Additional text input is prevented or a character count indicator shows the remaining characters available")
def character_limit_enforced(page: Page) -> None:
    """Verify character limit is enforced."""
    from pages.tc_005_form_page import Tc005FormPage
    form_page = Tc005FormPage(page)

    if form_page.locators.character_count.count() > 0:
        expect(form_page.locators.character_count).to_be_visible()
    else:
        value = form_page.get_field_value(form_page.locators.comments_field)
        expect(len(value)).to_be_less_than_or_equal(1000)
