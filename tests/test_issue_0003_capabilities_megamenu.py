"""Test runner for issue_0003: Implement Capabilities mega-menu."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0003_capabilities_megamenu_steps import *  # noqa: F401, F403

scenarios("issue_0003_capabilities_megamenu.feature")
