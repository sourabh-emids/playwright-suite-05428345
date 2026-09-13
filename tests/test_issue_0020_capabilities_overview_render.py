"""Test glue for issue_0020: Capabilities overview render"""

from pytest_bdd import scenarios

from tests.steps.issue_0020_capabilities_overview_render_steps import *
from tests.steps import common_steps

scenarios("issue_0020_capabilities_overview_render.feature")
