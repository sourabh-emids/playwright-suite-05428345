"""Test runner for issue_0006: Implement Company navigation group."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0006_company_nav_steps import *  # noqa: F401, F403

scenarios("issue_0006_company_nav.feature")
