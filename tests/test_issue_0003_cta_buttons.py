"""Tests for issue_0003: Primary CTA buttons function properly."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0003_cta_buttons_steps import *


scenarios("../features/issue_0003_cta_buttons.feature")
