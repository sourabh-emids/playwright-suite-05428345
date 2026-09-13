"""Tests for Five audience/industry entries rendering (issue_0024)."""
from tests.steps.issue_0024_who_we_serve_steps import *
from tests.steps.common_steps import *
from pytest_bdd import scenarios

scenarios("issue_0024_who_we_serve.feature")
