"""Tests for Final conversion banner rendering (issue_0034)."""
from tests.steps.issue_0034_final_cta_steps import *
from tests.steps.common_steps import *
from pytest_bdd import scenarios

scenarios("issue_0034_final_cta.feature")
