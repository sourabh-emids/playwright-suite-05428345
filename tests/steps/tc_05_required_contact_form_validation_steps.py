"""Step definitions for TC-05 contact-form validation."""
from playwright.sync_api import Page
from pytest_bdd import given, then, when

from pages.tc_05_required_contact_form_validation_page import (
    Tc05RequiredContactFormValidationPage,
)


@given("the TC-05 user opens the contact form with required fields empty")
def open_empty_contact_form(page: Page) -> None:
    Tc05RequiredContactFormValidationPage(page).open()


@when("the TC-05 user attempts to submit the incomplete contact form")
def submit_incomplete_contact_form(page: Page) -> None:
    Tc05RequiredContactFormValidationPage(page).attempt_empty_submission()


@then(
    "the TC-05 form remains unsubmitted and each required field shows a clear validation message"
)
def required_validation_is_displayed(page: Page) -> None:
    Tc05RequiredContactFormValidationPage(page).assert_empty_submission_is_blocked()
