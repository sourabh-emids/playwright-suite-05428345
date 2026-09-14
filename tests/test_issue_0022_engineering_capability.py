"""Test runner for issue_0022: Render Engineering capability content."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0022_engineering_capability_steps import *  # noqa: F401, F403

scenarios("issue_0022_engineering_capability.feature")
