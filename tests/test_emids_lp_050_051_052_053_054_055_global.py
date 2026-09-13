"""Test file for emids_lp_050-055: Global requirements."""
import pytest
from pytest_bdd import scenarios

from tests.steps.emids_lp_050_051_052_053_054_055_global_steps import *  # noqa: F401, F403

scenarios("../../tests/features/emids_lp_050_051_052_053_054_055_global.feature")
