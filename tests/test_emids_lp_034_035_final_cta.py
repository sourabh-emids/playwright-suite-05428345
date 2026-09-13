"""Test file for emids_lp_034-035: Final conversion banner and timeline."""
import pytest
from pytest_bdd import scenarios

from tests.steps.emids_lp_034_035_final_cta_steps import *  # noqa: F401, F403

scenarios("../../tests/features/emids_lp_034_035_final_cta.feature")
