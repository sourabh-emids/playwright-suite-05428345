"""Test runner for issue_0019: Reduced Motion for Partner Animation."""
from pytest_bdd import scenarios
from tests.steps.issue_0019_reduced_motion_partner_steps import *
from tests.steps.common_steps import *

scenarios("issue_0019_reduced_motion_partner.feature")
