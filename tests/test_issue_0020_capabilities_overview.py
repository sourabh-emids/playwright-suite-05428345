"""Test runner for issue_0020: Render capabilities overview."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0020_capabilities_overview_steps import *  # noqa: F401, F403

scenarios("issue_0020_capabilities_overview.feature")
