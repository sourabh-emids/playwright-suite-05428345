"""Tests for Insights navigation group implementation (issue_0005)."""
from tests.steps.issue_0005_insights_navigation_steps import *
from tests.steps.common_steps import *
from pytest_bdd import scenarios

scenarios("issue_0005_insights_navigation.feature")
