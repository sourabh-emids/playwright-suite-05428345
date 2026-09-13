"""Tests for Wistia and YouTube embeds (issues 0043-0044)."""
from tests.steps.issue_0043_0044_wistia_youtube_steps import *
from tests.steps.common_steps import *
from pytest_bdd import scenarios

scenarios("issue_0043_0044_wistia_youtube.feature")
