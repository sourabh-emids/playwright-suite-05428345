"""Test runner for issue_0033: Resource access handoff without false download implication."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0033_resource_access_steps import *  # noqa: F401, F403

scenarios("issue_0033_resource_access.feature")
