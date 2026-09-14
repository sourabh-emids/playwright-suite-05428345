"""Test runner for issue_0018: Render partner logo rail/marquee."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0018_partner_logos_steps import *  # noqa: F401, F403

scenarios("issue_0018_partner_logos.feature")
