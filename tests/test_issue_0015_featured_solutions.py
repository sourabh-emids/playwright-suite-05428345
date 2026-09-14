"""Test runner for issue_0015: Render six featured solution items."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0015_featured_solutions_steps import *  # noqa: F401, F403

scenarios("issue_0015_featured_solutions.feature")
