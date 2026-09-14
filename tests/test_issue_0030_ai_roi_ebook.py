"""Test runner for issue_0030: Display AI ROI eBook card."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0030_ai_roi_ebook_steps import *  # noqa: F401, F403

scenarios("issue_0030_ai_roi_ebook.feature")
