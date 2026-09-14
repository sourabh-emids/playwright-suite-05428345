"""Test runner for issue_0038: Support Google Analytics after consent."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0038_google_analytics_steps import *  # noqa: F401, F403

scenarios("issue_0038_google_analytics.feature")
