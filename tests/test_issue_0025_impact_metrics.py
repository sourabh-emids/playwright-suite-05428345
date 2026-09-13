"""Tests for Impact proof metrics rendering (issue_0025)."""
from tests.steps.issue_0025_impact_metrics_steps import *
from tests.steps.common_steps import *
from pytest_bdd import scenarios

scenarios("issue_0025_impact_metrics.feature")
