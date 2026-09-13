"""Test glue for issue_0004: Industries mega-menu implementation"""

from pytest_bdd import scenarios

from tests.steps.issue_0004_industries_mega_menu_implementation_steps import *
from tests.steps import common_steps

scenarios("issue_0004_industries_mega_menu_implementation.feature")
