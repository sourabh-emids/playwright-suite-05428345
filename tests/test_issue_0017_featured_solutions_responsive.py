"""Tests for Featured solution responsive interaction (issue_0017)."""
from tests.steps.issue_0017_featured_solutions_responsive_steps import *
from tests.steps.common_steps import *
from pytest_bdd import scenarios

scenarios("issue_0017_featured_solutions_responsive.feature")
