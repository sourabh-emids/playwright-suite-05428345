"""Step definitions for REQ-005: Contact form displays validation for required fields."""

from pytest_bdd import given, when, then  # noqa: F401

from pages.req_001_homepage_page import Req001HomepagePage
from utils.config import BASE_URL


@given("User navigates to and opens the contact form")
def user_navigates_to_contact_form(req005_contact_form_page) -> None:
    """Navigate to contact page."""
    homepage_page = Req001HomepagePage(req005_contact_form_page.page)
    homepage_page.goto_homepage(BASE_URL)
    homepage_page.dismiss_cookie_banner_if_present()
    req005_contact_form_page.goto_contact_page(BASE_URL)
    req005_contact_form_page.verify_form_visible()


@given("User is on the contact page")
def user_on_contact_page(req005_contact_form_page) -> None:
    """User is on contact page."""
    homepage_page = Req001HomepagePage(req005_contact_form_page.page)
    homepage_page.goto_homepage(BASE_URL)
    homepage_page.dismiss_cookie_banner_if_present()
    req005_contact_form_page.goto_contact_page(BASE_URL)


@given("User submits contact form with incomplete required fields")
def user_submits_incomplete_form(req005_contact_form_page) -> None:
    """Submit form with incomplete fields."""
    req005_contact_form_page.submit_empty_form()


@when("User submits the form with all required fields left empty")
def user_submits_empty_form(req005_contact_form_page) -> None:
    """Submit form with all fields empty."""
    req005_contact_form_page.submit_empty_form()


@then("Clear validation messages appear for each required field indicating they are mandatory")
def validation_messages_appear(req005_contact_form_page) -> None:
    """Verify validation messages appear for all required fields."""
    req005_contact_form_page.verify_validation_messages_appear_for_all_required_fields()


@when("Form validation is triggered")
def form_validation_triggered(req005_contact_form_page) -> None:
    """Wait for form validation to complete."""
    pass


@then("The form is not submitted and appropriate error messaging guides user to complete required fields")
def form_not_submitted(req005_contact_form_page) -> None:
    """Verify form was not submitted."""
    req005_contact_form_page.verify_form_not_submitted()


@when("User submits the form without filling First Name")
def user_submits_without_first_name(req005_contact_form_page) -> None:
    """Submit form without First Name."""
    req005_contact_form_page.submit_empty_form()


@then("The First Name field should show validation message \"This field is required\"")
def first_name_validation_shown(req005_contact_form_page) -> None:
    """Verify First Name validation message appears."""
    req005_contact_form_page.verify_first_name_has_validation()


@when("User submits the form without filling Work Email")
def user_submits_without_work_email(req005_contact_form_page) -> None:
    """Submit form without Work Email."""
    req005_contact_form_page.submit_empty_form()


@then("The Work Email field should show validation message \"This field is required\"")
def work_email_validation_shown(req005_contact_form_page) -> None:
    """Verify Work Email validation message appears."""
    req005_contact_form_page.verify_work_email_has_validation()


@when("User submits the form without filling Company Name")
def user_submits_without_company_name(req005_contact_form_page) -> None:
    """Submit form without Company Name."""
    req005_contact_form_page.submit_empty_form()


@then("The Company Name field should show validation message \"This field is required\"")
def company_name_validation_shown(req005_contact_form_page) -> None:
    """Verify Company Name validation message appears."""
    req005_contact_form_page.verify_company_name_has_validation()
