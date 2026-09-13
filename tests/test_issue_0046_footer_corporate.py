"""Tests for Footer corporate and contact information (issue_0046)."""
from tests.steps.issue_0046_footer_corporate_steps import *
from tests.steps.common_steps import *
from pytest_bdd import scenarios

scenarios("issue_0046_footer_corporate.feature")
