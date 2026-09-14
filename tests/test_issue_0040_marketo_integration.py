"""Test runner for issue_0040: Integrate Marketo with consent."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0040_marketo_integration_steps import *  # noqa: F401, F403

scenarios("issue_0040_marketo_integration.feature")
