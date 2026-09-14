"""Test runner for issue_0016: Provide All Solutions CTA."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0016_all_solutions_cta_steps import *  # noqa: F401, F403

scenarios("issue_0016_all_solutions_cta.feature")
