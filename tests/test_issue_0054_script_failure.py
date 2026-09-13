"""Tests for Script failure resilience (issue_0054)."""
from tests.steps.issue_0054_script_failure_steps import *
from tests.steps.common_steps import *
from pytest_bdd import scenarios

scenarios("issue_0054_script_failure.feature")
