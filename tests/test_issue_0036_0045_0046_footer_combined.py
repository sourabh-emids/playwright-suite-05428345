"""Test glue for issue_0036, 0045-0046: Footer combined"""

from pytest_bdd import scenarios

from tests.steps.issue_0036_0045_0046_footer_combined_steps import *
from tests.steps import common_steps

scenarios("issue_0036_0045_0046_footer_combined.feature")
