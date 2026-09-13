"""Tests for WCAG 2.1 AA compliance (issue_0050)."""
from tests.steps.issue_0050_wcag_compliance_steps import *
from tests.steps.common_steps import *
from pytest_bdd import scenarios

scenarios("issue_0050_wcag_compliance.feature")
