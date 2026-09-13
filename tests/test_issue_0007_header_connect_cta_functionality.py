"""Test glue for issue_0007: Header Connect CTA functionality"""

from pytest_bdd import scenarios

from tests.steps.issue_0007_header_connect_cta_functionality_steps import *
from tests.steps import common_steps

scenarios("issue_0007_header_connect_cta_functionality.feature")
