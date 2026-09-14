"""Test runner for issue_0048: Support Inquiry Type enum values."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0048_inquiry_type_enum_steps import *  # noqa: F401, F403

scenarios("issue_0048_inquiry_type_enum.feature")
