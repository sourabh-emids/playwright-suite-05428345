"""Test glue for issue_0019: Reduced motion for partner animation"""

from pytest_bdd import scenarios

from tests.steps.issue_0019_reduced_motion_for_partner_animation_steps import *
from tests.steps import common_steps

scenarios("issue_0019_reduced_motion_for_partner_animation.feature")
