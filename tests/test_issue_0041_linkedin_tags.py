"""Test runner for issue_0041: Integrate LinkedIn tags conditionally."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0041_linkedin_tags_steps import *  # noqa: F401, F403

scenarios("issue_0041_linkedin_tags.feature")
