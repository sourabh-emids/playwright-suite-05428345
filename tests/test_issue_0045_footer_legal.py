"""Tests for Footer legal navigation rendering (issue_0045)."""
from tests.steps.issue_0045_footer_legal_steps import *
from tests.steps.common_steps import *
from pytest_bdd import scenarios

scenarios("issue_0045_footer_legal.feature")
