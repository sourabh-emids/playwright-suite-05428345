"""Test runner for issue_0004: Implement Industries mega-menu."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0004_industries_megamenu_steps import *  # noqa: F401, F403

scenarios("issue_0004_industries_megamenu.feature")
