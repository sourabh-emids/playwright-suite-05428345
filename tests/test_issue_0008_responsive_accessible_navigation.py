"""Test glue for issue_0008: Responsive accessible navigation"""

from pytest_bdd import scenarios

from tests.steps.issue_0008_responsive_accessible_navigation_steps import *
from tests.steps import common_steps

scenarios("issue_0008_responsive_accessible_navigation.feature")
