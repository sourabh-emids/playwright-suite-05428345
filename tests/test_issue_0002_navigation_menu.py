"""Tests for issue_0002: Main navigation menu items work correctly."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0002_navigation_menu_steps import *


scenarios("../features/issue_0002_navigation_menu.feature")
