"""Test runner for issue_0010: Route hero CTA to FDCE experience."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0010_hero_cta_fdce_steps import *  # noqa: F401, F403

scenarios("issue_0010_hero_cta_fdce.feature")
