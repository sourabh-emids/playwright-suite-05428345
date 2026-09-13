"""Tests for Global header visibility and Emids brand link (issue_0001)."""
from tests.steps.issue_0001_header_visibility_steps import *
from tests.steps.common_steps import *
from pytest_bdd import scenarios

scenarios("issue_0001_header_visibility.feature")
