"""Test runner for issue_0029: Display Life Sciences eBook card."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0029_life_sciences_ebook_steps import *  # noqa: F401, F403

scenarios("issue_0029_life_sciences_ebook.feature")
