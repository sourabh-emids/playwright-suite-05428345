"""Test runner for issue_0039: Implement campaign attribution safely."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0039_campaign_attribution_steps import *  # noqa: F401, F403

scenarios("issue_0039_campaign_attribution.feature")
