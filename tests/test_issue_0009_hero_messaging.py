"""Test runner for issue_0009: Hero Messaging and Visual Rendering."""
from pytest_bdd import scenarios
from tests.steps.issue_0009_hero_messaging_steps import *
from tests.steps.common_steps import *

scenarios("issue_0009_hero_messaging.feature")
