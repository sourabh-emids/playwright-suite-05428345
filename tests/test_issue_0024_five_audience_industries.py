"""Test runner for issues 0024-0033: Audience, Impact, and Insights modules."""
from pytest_bdd import scenarios
from tests.steps.issue_0024_five_audience_industries_steps import *
from tests.steps.common_steps import *

scenarios("issue_0024_five_audience_industries.feature")
