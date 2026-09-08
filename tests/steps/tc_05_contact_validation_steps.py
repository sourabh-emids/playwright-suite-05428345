import pytest
from playwright.sync_api import Page
from pytest_bdd import given, then, when

from pages.tc_05_contact_validation_page import Tc05ContactValidationPage


@pytest.fixture
def tc_05_contact_form(page: Page) -> Tc05ContactValidationPage:
    return Tc05ContactValidationPage(page)


@given("the Emids contact form is open with every required field empty")
def open_empty_contact_form(
    tc_05_contact_form: Tc05ContactValidationPage,
) -> None:
    tc_05_contact_form.open()
    tc_05_contact_form.assert_required_fields_empty()


@when("I submit the empty contact form")
def submit_empty_contact_form(
    tc_05_contact_form: Tc05ContactValidationPage,
) -> None:
    tc_05_contact_form.submit()


@then("the contact form submission is rejected")
def verify_submission_rejected(
    tc_05_contact_form: Tc05ContactValidationPage,
) -> None:
    tc_05_contact_form.assert_submission_rejected()


@then("every empty required field provides clear validation feedback")
def verify_required_field_feedback(
    tc_05_contact_form: Tc05ContactValidationPage,
) -> None:
    tc_05_contact_form.assert_required_field_feedback()
