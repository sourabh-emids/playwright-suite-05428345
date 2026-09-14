"""Test runner for issue_0049: Contact form submission feedback and retry."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0049_contact_form_feedback_steps import *  # noqa: F401, F403

scenarios("issue_0049_contact_form_feedback.feature")
