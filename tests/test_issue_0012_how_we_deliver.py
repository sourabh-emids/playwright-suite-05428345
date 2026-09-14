"""Test runner for issue_0012: How We Deliver Section Rendering."""
from pytest_bdd import scenarios
from tests.steps.issue_0012_how_we_deliver_steps import *
from tests.steps.common_steps import *

scenarios("issue_0012_how_we_deliver.feature")
