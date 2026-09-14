"""Test runner for issue_0018: Partner Logo Rail/Marquee Rendering."""
from pytest_bdd import scenarios
from tests.steps.issue_0018_partner_logo_rail_steps import *
from tests.steps.common_steps import *

scenarios("issue_0018_partner_logo_rail.feature")
