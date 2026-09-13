"""Test glue for issue_0015: Render six featured solutions"""

from pytest_bdd import scenarios

from tests.steps.issue_0015_render_six_featured_solutions_steps import *
from tests.steps import common_steps

scenarios("issue_0015_render_six_featured_solutions.feature")
