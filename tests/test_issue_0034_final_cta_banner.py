"""Test runner for issue_0034: Render final conversion banner."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0034_final_cta_banner_steps import *  # noqa: F401, F403

scenarios("issue_0034_final_cta_banner.feature")
