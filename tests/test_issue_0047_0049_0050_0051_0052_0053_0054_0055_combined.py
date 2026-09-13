"""Test glue for remaining issues combined"""

from pytest_bdd import scenarios

from tests.steps.issue_0047_0049_0050_0051_0052_0053_0054_0055_combined_steps import *
from tests.steps import common_steps

scenarios("issue_0047_0049_0050_0051_0052_0053_0054_0055_combined.feature")
