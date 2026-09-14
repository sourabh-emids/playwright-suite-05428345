"""Test runner for issue_0013: Provide See the model CTA."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0013_see_model_cta_steps import *  # noqa: F401, F403

scenarios("issue_0013_see_model_cta.feature")
