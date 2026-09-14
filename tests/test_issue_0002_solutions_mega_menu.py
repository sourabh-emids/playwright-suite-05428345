"""Test runner for issue_0002: Solutions Mega-Menu Implementation."""
from pytest_bdd import scenarios
from tests.steps.issue_0002_solutions_mega_menu_steps import *
from tests.steps.common_steps import *

scenarios("issue_0002_solutions_mega_menu.feature")
