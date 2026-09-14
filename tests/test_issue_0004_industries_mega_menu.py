"""Test runner for issue_0004: Industries Mega-Menu Implementation."""
from pytest_bdd import scenarios
from tests.steps.issue_0004_industries_mega_menu_steps import *
from tests.steps.common_steps import *

scenarios("issue_0004_industries_mega_menu.feature")
