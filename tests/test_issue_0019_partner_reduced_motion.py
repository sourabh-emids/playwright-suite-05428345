"""Test runner for issue_0019: Respect reduced motion for partner animation."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0019_partner_reduced_motion_steps import *  # noqa: F401, F403

scenarios("issue_0019_partner_reduced_motion.feature")
