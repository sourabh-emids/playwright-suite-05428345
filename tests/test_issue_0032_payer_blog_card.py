"""Test runner for issue_0032: Display Payer data readiness blog card."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0032_payer_blog_card_steps import *  # noqa: F401, F403

scenarios("issue_0032_payer_blog_card.feature")
