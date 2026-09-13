"""Test file for emids_lp_023: Render Platforms capability content."""
import pytest
from pytest_bdd import scenarios

from tests.steps.emids_lp_023_platforms_capability_steps import *  # noqa: F401, F403

scenarios("../../tests/features/emids_lp_023_platforms_capability.feature")
