"""Test glue for issue_0024: Five audience entries render"""

from pytest_bdd import scenarios

from tests.steps.issue_0024_five_audience_entries_render_steps import *
from tests.steps import common_steps

scenarios("issue_0024_five_audience_entries_render.feature")
