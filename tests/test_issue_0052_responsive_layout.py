"""Tests for Responsive layout across viewports (issue_0052)."""
from tests.steps.issue_0052_responsive_layout_steps import *
from tests.steps.common_steps import *
from pytest_bdd import scenarios

scenarios("issue_0052_responsive_layout.feature")
