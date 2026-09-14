"""Test runner for issue_0010: Hero CTA Routes to FDCE Experience."""
from pytest_bdd import scenarios
from tests.steps.issue_0010_hero_cta_fdce_steps import *
from tests.steps.common_steps import *

scenarios("issue_0010_hero_cta_fdce.feature")
