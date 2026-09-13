"""Tests for Capabilities overview rendering (issue_0020)."""
from tests.steps.issue_0020_capabilities_overview_steps import *
from tests.steps.common_steps import *
from pytest_bdd import scenarios

scenarios("issue_0020_capabilities_overview.feature")
