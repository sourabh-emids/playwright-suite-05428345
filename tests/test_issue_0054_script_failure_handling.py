"""Test runner for issue_0054: Handle script failures without breaking content."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0054_script_failure_handling_steps import *  # noqa: F401, F403

scenarios("issue_0054_script_failure_handling.feature")
