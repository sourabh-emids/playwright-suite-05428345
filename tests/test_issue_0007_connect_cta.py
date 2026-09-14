"""Test runner for issue_0007: Provide header Connect CTA."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0007_connect_cta_steps import *  # noqa: F401, F403

scenarios("issue_0007_connect_cta.feature")
