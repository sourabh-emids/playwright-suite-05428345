"""Test runner for issue_0036: Expose Cookie Preferences control."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0036_cookie_preferences_steps import *  # noqa: F401, F403

scenarios("issue_0036_cookie_preferences.feature")
