"""Test runner for issue_0016: All Solutions CTA Rendering."""
from pytest_bdd import scenarios
from tests.steps.issue_0016_all_solutions_cta_steps import *
from tests.steps.common_steps import *

scenarios("issue_0016_all_solutions_cta.feature")
