"""Test file for emids_lp_020: Render capabilities overview."""
import pytest
from pytest_bdd import scenarios

from tests.steps.emids_lp_020_capabilities_overview_steps import *  # noqa: F401, F403

scenarios("../../tests/features/emids_lp_020_capabilities_overview.feature")
