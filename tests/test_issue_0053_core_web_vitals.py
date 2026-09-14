"""Test runner for issue_0053: Meet Core Web Vitals performance goals."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0053_core_web_vitals_steps import *  # noqa: F401, F403

scenarios("issue_0053_core_web_vitals.feature")
