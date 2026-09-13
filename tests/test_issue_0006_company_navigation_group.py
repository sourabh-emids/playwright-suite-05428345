"""Test glue for issue_0006: Company navigation group"""

from pytest_bdd import scenarios

from tests.steps.issue_0006_company_navigation_group_steps import *
from tests.steps import common_steps

scenarios("issue_0006_company_navigation_group.feature")
