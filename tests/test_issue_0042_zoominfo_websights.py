"""Test runner for issue_0042: Integrate ZoomInfo WebSights conditionally."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0042_zoominfo_websights_steps import *  # noqa: F401, F403

scenarios("issue_0042_zoominfo_websights.feature")
