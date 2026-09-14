"""Test runner for issue_0015: Six Featured Solution Items."""
from pytest_bdd import scenarios
from tests.steps.issue_0015_six_featured_solutions_steps import *
from tests.steps.common_steps import *

scenarios("issue_0015_six_featured_solutions.feature")
