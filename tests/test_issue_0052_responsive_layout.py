"""Test runner for issue_0052: Provide responsive layout across viewports."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0052_responsive_layout_steps import *  # noqa: F401, F403

scenarios("issue_0052_responsive_layout.feature")
