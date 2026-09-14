"""Test runner for issue_0023: Render Platforms capability content."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0023_platforms_capability_steps import *  # noqa: F401, F403

scenarios("issue_0023_platforms_capability.feature")
