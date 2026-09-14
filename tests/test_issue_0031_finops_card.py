"""Test runner for issue_0031: Display FinOps healthcare payer card."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0031_finops_card_steps import *  # noqa: F401, F403

scenarios("issue_0031_finops_card.feature")
