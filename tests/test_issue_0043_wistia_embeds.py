"""Test runner for issue_0043: Support Wistia embeds when configured."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0043_wistia_embeds_steps import *  # noqa: F401, F403

scenarios("issue_0043_wistia_embeds.feature")
