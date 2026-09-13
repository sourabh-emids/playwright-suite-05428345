"""Test glue for issue_0034-0035: Final CTA combined"""

from pytest_bdd import scenarios

from tests.steps.issue_0034_0035_final_cta_combined_steps import *
from tests.steps import common_steps

scenarios("issue_0034_0035_final_cta_combined.feature")
