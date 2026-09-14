"""Test runner for issues 0034-0046: Final CTA, Footer, and Analytics Modules."""
from pytest_bdd import scenarios
from tests.steps.issue_0034_final_cta_banner_steps import *
from tests.steps.common_steps import *

scenarios("issue_0034_final_cta_banner.feature")
