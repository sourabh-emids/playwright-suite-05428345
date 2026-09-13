"""Test glue for issue_0013: See the model CTA functionality"""

from pytest_bdd import scenarios

from tests.steps.issue_0013_see_the_model_cta_functionality_steps import *
from tests.steps import common_steps

scenarios("issue_0013_see_the_model_cta_functionality.feature")
