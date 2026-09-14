"""Test runner for issue_0007: Header Connect CTA Functionality."""
from pytest_bdd import scenarios
from tests.steps.issue_0007_header_connect_cta_steps import *
from tests.steps.common_steps import *

scenarios("issue_0007_header_connect_cta.feature")
