"""Test runner for issue_0017: Support featured-solution responsive interaction."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0017_featured_solutions_responsive_steps import *  # noqa: F401, F403

scenarios("issue_0017_featured_solutions_responsive.feature")
