"""Test runner for issue_0002: Implement Solutions mega-menu."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0002_solutions_megamenu_steps import *  # noqa: F401, F403

scenarios("issue_0002_solutions_megamenu.feature")
