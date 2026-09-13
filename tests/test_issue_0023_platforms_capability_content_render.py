"""Test glue for issue_0023: Platforms capability content render"""

from pytest_bdd import scenarios

from tests.steps.issue_0023_platforms_capability_content_render_steps import *
from tests.steps import common_steps

scenarios("issue_0023_platforms_capability_content_render.feature")
