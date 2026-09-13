"""Test file for emids_lp_015: Render six featured solution items."""
import pytest
from pytest_bdd import scenarios

from tests.steps.emids_lp_015_featured_solutions_steps import *  # noqa: F401, F403

scenarios("../../tests/features/emids_lp_015_featured_solutions.feature")
