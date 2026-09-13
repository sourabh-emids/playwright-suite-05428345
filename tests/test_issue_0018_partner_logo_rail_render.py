"""Test glue for issue_0018: Partner logo rail render"""

from pytest_bdd import scenarios

from tests.steps.issue_0018_partner_logo_rail_render_steps import *
from tests.steps import common_steps

scenarios("issue_0018_partner_logo_rail_render.feature")
