"""Test runner for issue_0005: Implement Insights navigation group."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0005_insights_nav_steps import *  # noqa: F401, F403

scenarios("issue_0005_insights_nav.feature")
