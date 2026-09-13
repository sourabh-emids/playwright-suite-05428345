"""Test glue for issue_0037-0044: Analytics and Media combined"""

from pytest_bdd import scenarios

from tests.steps.issue_0037_0042_analytics_media_combined_steps import *
from tests.steps import common_steps

scenarios("issue_0037_0042_analytics_media_combined.feature")
