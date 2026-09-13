"""Test glue for issue_0012: How We Deliver section render"""

from pytest_bdd import scenarios

from tests.steps.issue_0012_how_we_deliver_section_render_steps import *
from tests.steps import common_steps

scenarios("issue_0012_how_we_deliver_section_render.feature")
