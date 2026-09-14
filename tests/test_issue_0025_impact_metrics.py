"""Test runner for issue_0025: Render Impact proof metrics."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0025_impact_metrics_steps import *  # noqa: F401, F403

scenarios("issue_0025_impact_metrics.feature")
