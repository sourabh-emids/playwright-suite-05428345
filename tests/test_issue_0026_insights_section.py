"""Tests for Insights section and six content cards (issue_0026)."""
from tests.steps.issue_0026_insights_section_steps import *
from tests.steps.common_steps import *
from pytest_bdd import scenarios

scenarios("issue_0026_insights_section.feature")
