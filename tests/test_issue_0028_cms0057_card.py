"""Test runner for issue_0028: Display CMS-0057 interoperability card."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0028_cms0057_card_steps import *  # noqa: F401, F403

scenarios("issue_0028_cms0057_card.feature")
