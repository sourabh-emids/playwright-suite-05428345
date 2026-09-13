"""Test file for emids_lp_021: Render AI capability content."""
import pytest
from pytest_bdd import scenarios

from tests.steps.emids_lp_021_ai_capability_steps import *  # noqa: F401, F403

scenarios("../../tests/features/emids_lp_021_ai_capability.feature")
