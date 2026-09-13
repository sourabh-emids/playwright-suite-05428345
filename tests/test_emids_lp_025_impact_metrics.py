"""Test file for emids_lp_025: Render Impact proof metrics."""
import pytest
from pytest_bdd import scenarios

from tests.steps.emids_lp_025_impact_metrics_steps import *  # noqa: F401, F403

scenarios("../../tests/features/emids_lp_025_impact_metrics.feature")
