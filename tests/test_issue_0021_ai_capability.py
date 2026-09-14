"""Test runner for issue_0021: Render AI capability content."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0021_ai_capability_steps import *  # noqa: F401, F403

scenarios("issue_0021_ai_capability.feature")
