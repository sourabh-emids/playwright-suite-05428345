"""Test runner for issue_0044: Support YouTube embeds when configured."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0044_youtube_embeds_steps import *  # noqa: F401, F403

scenarios("issue_0044_youtube_embeds.feature")
