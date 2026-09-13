"""Tests for How We Deliver section rendering (issue_0012)."""
from tests.steps.issue_0012_how_we_deliver_steps import *
from tests.steps.common_steps import *
from pytest_bdd import scenarios

scenarios("issue_0012_how_we_deliver.feature")
