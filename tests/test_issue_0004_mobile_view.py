"""Tests for issue_0004: Mobile responsive layout is usable."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0004_mobile_view_steps import *


scenarios("../features/issue_0004_mobile_view.feature")
