"""Test runner for issue_0006: Company Navigation Group."""
from pytest_bdd import scenarios
from tests.steps.issue_0006_company_navigation_group_steps import *
from tests.steps.common_steps import *

scenarios("issue_0006_company_navigation_group.feature")
