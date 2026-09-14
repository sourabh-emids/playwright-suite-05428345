"""Test runner for issue_0045: Render footer legal navigation."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0045_footer_legal_nav_steps import *  # noqa: F401, F403

scenarios("issue_0045_footer_legal_nav.feature")
