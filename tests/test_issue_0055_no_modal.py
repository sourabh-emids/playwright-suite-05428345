"""Tests for No promotional modal in base experience (issue_0055)."""
from tests.steps.issue_0055_no_modal_steps import *
from tests.steps.common_steps import *
from pytest_bdd import scenarios

scenarios("issue_0055_no_modal.feature")
