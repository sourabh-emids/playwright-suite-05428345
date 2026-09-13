"""Tests for See the model CTA functionality (issue_0013)."""
from tests.steps.issue_0013_see_model_cta_steps import *
from tests.steps.common_steps import *
from pytest_bdd import scenarios

scenarios("issue_0013_see_model_cta.feature")
