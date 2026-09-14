"""Test runner for issue_0011: Optimize hero media loading."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0011_hero_media_optimization_steps import *  # noqa: F401, F403

scenarios("issue_0011_hero_media_optimization.feature")
