"""Tests for Hero messaging and visual rendering (issue_0009)."""
from tests.steps.issue_0009_hero_messaging_steps import *
from tests.steps.common_steps import *
from pytest_bdd import scenarios

scenarios("issue_0009_hero_messaging.feature")
