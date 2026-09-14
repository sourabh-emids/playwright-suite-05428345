"""Test runner for issue_0008: Provide responsive accessible navigation."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0008_responsive_nav_steps import *  # noqa: F401, F403

scenarios("issue_0008_responsive_nav.feature")
