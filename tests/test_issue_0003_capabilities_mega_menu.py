"""Test runner for issue_0003: Capabilities Mega-Menu Implementation."""
from pytest_bdd import scenarios
from tests.steps.issue_0003_capabilities_mega_menu_steps import *
from tests.steps.common_steps import *

scenarios("issue_0003_capabilities_mega_menu.feature")
