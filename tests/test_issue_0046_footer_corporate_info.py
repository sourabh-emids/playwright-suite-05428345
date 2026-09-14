"""Test runner for issue_0046: Render footer corporate contact information."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0046_footer_corporate_info_steps import *  # noqa: F401, F403

scenarios("issue_0046_footer_corporate_info.feature")
