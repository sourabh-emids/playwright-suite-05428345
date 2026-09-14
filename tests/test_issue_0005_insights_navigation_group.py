"""Test runner for issue_0005: Insights Navigation Group."""
from pytest_bdd import scenarios
from tests.steps.issue_0005_insights_navigation_group_steps import *
from tests.steps.common_steps import *

scenarios("issue_0005_insights_navigation_group.feature")
