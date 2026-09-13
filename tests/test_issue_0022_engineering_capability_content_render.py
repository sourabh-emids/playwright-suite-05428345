"""Test glue for issue_0022: Engineering capability content render"""

from pytest_bdd import scenarios

from tests.steps.issue_0022_engineering_capability_content_render_steps import *
from tests.steps import common_steps

scenarios("issue_0022_engineering_capability_content_render.feature")
