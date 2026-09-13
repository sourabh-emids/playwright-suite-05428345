"""Tests for Company navigation group implementation (issue_0006)."""
from tests.steps.issue_0006_company_navigation_steps import *
from tests.steps.common_steps import *
from pytest_bdd import scenarios

scenarios("issue_0006_company_navigation.feature")
