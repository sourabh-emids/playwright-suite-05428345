"""Test runner for issue_0026: Render Insights section with six cards."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0026_insights_section_steps import *  # noqa: F401, F403

scenarios("issue_0026_insights_section.feature")
