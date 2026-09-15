"""Tests for issue_0001: Homepage loads without errors."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0001_homepage_loading_steps import *


scenarios("../features/issue_0001_homepage_loading.feature")
