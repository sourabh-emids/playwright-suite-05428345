"""Test runner for issue_0009: Render hero messaging and visual."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0009_hero_messaging_steps import *  # noqa: F401, F403

scenarios("issue_0009_hero_messaging.feature")
