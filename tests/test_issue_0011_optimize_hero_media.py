"""Test runner for issue_0011: Optimize Hero Media Loading."""
from pytest_bdd import scenarios
from tests.steps.issue_0011_optimize_hero_media_steps import *
from tests.steps.common_steps import *

scenarios("issue_0011_optimize_hero_media.feature")
