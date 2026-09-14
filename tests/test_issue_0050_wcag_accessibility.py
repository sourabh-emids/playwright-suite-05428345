"""Test runner for issue_0050: Meet WCAG 2.1 AA accessibility target."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0050_wcag_accessibility_steps import *  # noqa: F401, F403

scenarios("issue_0050_wcag_accessibility.feature")
