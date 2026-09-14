"""Test runner for issue_0055: Base homepage without unsolicited modal."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0055_no_unsolicited_modal_steps import *  # noqa: F401, F403

scenarios("issue_0055_no_unsolicited_modal.feature")
