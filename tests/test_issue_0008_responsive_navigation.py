"""Tests for Responsive and accessible navigation behavior (issue_0008)."""
from tests.steps.issue_0008_responsive_navigation_steps import *
from tests.steps.common_steps import *
from pytest_bdd import scenarios

scenarios("issue_0008_responsive_navigation.feature")
