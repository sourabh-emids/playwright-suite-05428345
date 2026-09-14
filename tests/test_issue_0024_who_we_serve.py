"""Test runner for issue_0024: Render five audience/industry entries."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0024_who_we_serve_steps import *  # noqa: F401, F403

scenarios("issue_0024_who_we_serve.feature")
