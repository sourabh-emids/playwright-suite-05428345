"""Test runner for issues 0020-0023: Capabilities Module."""
from pytest_bdd import scenarios
from tests.steps.issue_0020_capabilities_overview_steps import *
from tests.steps.common_steps import *

scenarios("issue_0020_capabilities_overview.feature")
