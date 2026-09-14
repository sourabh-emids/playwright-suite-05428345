"""Test runner for issue_0008: Responsive Accessible Navigation Behavior."""
from pytest_bdd import scenarios
from tests.steps.issue_0008_responsive_accessible_navigation_steps import *
from tests.steps.common_steps import *

scenarios("issue_0008_responsive_accessible_navigation.feature")
