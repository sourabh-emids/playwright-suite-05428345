"""Tests for Performance and Core Web Vitals goals (issue_0053)."""
from tests.steps.issue_0053_performance_steps import *
from tests.steps.common_steps import *
from pytest_bdd import scenarios

scenarios("issue_0053_performance.feature")
