"""Test glue for issue_0025: Impact metrics render correctly"""

from pytest_bdd import scenarios

from tests.steps.issue_0025_impact_metrics_render_correctly_steps import *
from tests.steps import common_steps

scenarios("issue_0025_impact_metrics_render_correctly.feature")
