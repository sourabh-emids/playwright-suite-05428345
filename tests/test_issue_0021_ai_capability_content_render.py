"""Test glue for issue_0021: AI capability content render"""

from pytest_bdd import scenarios

from tests.steps.issue_0021_ai_capability_content_render_steps import *
from tests.steps import common_steps

scenarios("issue_0021_ai_capability_content_render.feature")
