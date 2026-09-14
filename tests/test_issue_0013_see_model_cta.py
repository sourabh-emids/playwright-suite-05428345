"""Test runner for issue_0013: See the Model CTA Implementation."""
from pytest_bdd import scenarios
from tests.steps.issue_0013_see_model_cta_steps import *
from tests.steps.common_steps import *

scenarios("issue_0013_see_model_cta.feature")
