"""Test glue file for REQ-005: Contact form displays validation for required fields."""

from pytest_bdd import scenarios

from tests.steps.req_005_contact_form_validation_steps import *  # noqa: F401,F403

scenarios("req_005_contact_form_validation.feature")
