"""Test runner for issue_0017: Featured Solution Responsive Interaction."""
from pytest_bdd import scenarios
from tests.steps.issue_0017_featured_solution_responsive_steps import *
from tests.steps.common_steps import *

scenarios("issue_0017_featured_solution_responsive.feature")
