"""Test glue for issue_0003: Capabilities mega-menu implementation"""

from pytest_bdd import scenarios

from tests.steps.issue_0003_capabilities_mega_menu_implementation_steps import *
from tests.steps import common_steps

scenarios("issue_0003_capabilities_mega_menu_implementation.feature")
