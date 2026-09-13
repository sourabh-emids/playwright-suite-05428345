"""Test glue for issue_0027-0033: Insight cards combined"""

from pytest_bdd import scenarios

from tests.steps.issue_0027_0033_insight_cards_combined_steps import *
from tests.steps import common_steps

scenarios("issue_0027_0033_insight_cards_combined.feature")
