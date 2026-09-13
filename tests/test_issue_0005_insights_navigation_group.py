"""Test glue for issue_0005: Insights navigation group"""

from pytest_bdd import scenarios

from tests.steps.issue_0005_insights_navigation_group_steps import *
from tests.steps import common_steps

scenarios("issue_0005_insights_navigation_group.feature")
