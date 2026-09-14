"""Test runner for issue_0027: Display Medicare Advantage eBook card."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0027_medicare_ebook_steps import *  # noqa: F401, F403

scenarios("issue_0027_medicare_ebook.feature")
