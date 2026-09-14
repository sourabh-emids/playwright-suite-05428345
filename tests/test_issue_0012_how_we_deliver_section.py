"""Test runner for issue_0012: Render How We Deliver section."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0012_how_we_deliver_section_steps import *  # noqa: F401, F403

scenarios("issue_0012_how_we_deliver_section.feature")
