"""Tests for Reduced motion for partner animation (issue_0019)."""
from tests.steps.issue_0019_reduced_motion_partners_steps import *
from tests.steps.common_steps import *
from pytest_bdd import scenarios

scenarios("issue_0019_reduced_motion_partners.feature")
