"""Test glue for issue_0002: Solutions mega-menu functionality"""

from pytest_bdd import scenarios

from tests.steps.issue_0002_solutions_mega_menu_functionality_steps import *
from tests.steps import common_steps

scenarios("issue_0002_solutions_mega_menu_functionality.feature")
