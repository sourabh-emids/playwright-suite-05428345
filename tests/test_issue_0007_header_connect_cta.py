"""Tests for Header Connect CTA functionality (issue_0007)."""
from tests.steps.issue_0007_header_connect_cta_steps import *
from tests.steps.common_steps import *
from pytest_bdd import scenarios

scenarios("issue_0007_header_connect_cta.feature")
