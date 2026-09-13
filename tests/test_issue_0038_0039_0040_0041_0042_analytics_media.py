"""Tests for Analytics and media conditional loading (issues 0038-0042)."""
from tests.steps.issue_0038_0039_0040_0041_0042_analytics_media_steps import *
from tests.steps.common_steps import *
from pytest_bdd import scenarios

scenarios("issue_0038_0039_0040_0041_0042_analytics_media.feature")
