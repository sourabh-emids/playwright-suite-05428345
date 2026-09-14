"""Test runner for issue_0047: Provide contact form with required fields."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0047_contact_form_steps import *  # noqa: F401, F403

scenarios("issue_0047_contact_form.feature")
