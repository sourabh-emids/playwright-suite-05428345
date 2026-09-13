"""Test file for emids_lp_017: Support featured-solution responsive interaction."""
import pytest
from pytest_bdd import scenarios

from tests.steps.emids_lp_017_responsive_solutions_steps import *  # noqa: F401, F403

scenarios("../../tests/features/emids_lp_017_responsive_solutions.feature")
