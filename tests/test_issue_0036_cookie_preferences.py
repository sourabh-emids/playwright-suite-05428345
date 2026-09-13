"""Tests for Cookie Preferences control exposure (issue_0036)."""
from tests.steps.issue_0036_cookie_preferences_steps import *
from tests.steps.common_steps import *
from pytest_bdd import scenarios

scenarios("issue_0036_cookie_preferences.feature")
