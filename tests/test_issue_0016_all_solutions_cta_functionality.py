"""Test glue for issue_0016: All Solutions CTA functionality"""

from pytest_bdd import scenarios

from tests.steps.issue_0016_all_solutions_cta_functionality_steps import *
from tests.steps import common_steps

scenarios("issue_0016_all_solutions_cta_functionality.feature")
