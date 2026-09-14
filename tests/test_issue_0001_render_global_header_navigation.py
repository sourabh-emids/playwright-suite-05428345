"""Test runner for issue_0001: Render Global Header Navigation."""
from pytest_bdd import scenarios
from tests.steps.issue_0001_render_global_header_navigation_steps import *
from tests.steps.common_steps import *

scenarios("issue_0001_render_global_header_navigation.feature")
