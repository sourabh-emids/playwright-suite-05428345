"""Test runner for issue_0035: Render delivery timing message."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0035_delivery_timing_steps import *  # noqa: F401, F403

scenarios("issue_0035_delivery_timing.feature")
