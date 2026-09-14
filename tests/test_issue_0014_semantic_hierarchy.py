"""Test runner for issue_0014: Maintain semantic section hierarchy."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0014_semantic_hierarchy_steps import *  # noqa: F401, F403

scenarios("issue_0014_semantic_hierarchy.feature")
