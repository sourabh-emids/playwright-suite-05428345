"""Test file for emids_lp_019: Respect reduced motion for partner animation."""
import pytest
from pytest_bdd import scenarios

from tests.steps.emids_lp_019_reduced_motion_partner_steps import *  # noqa: F401, F403

scenarios("../../tests/features/emids_lp_019_reduced_motion_partner.feature")
