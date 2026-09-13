"""Tests for Hero media loading optimization (issue_0011)."""
from tests.steps.issue_0011_hero_media_optimization_steps import *
from tests.steps.common_steps import *
from pytest_bdd import scenarios

scenarios("issue_0011_hero_media_optimization.feature")
