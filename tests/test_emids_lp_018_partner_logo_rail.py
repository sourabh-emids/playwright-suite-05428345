"""Test file for emids_lp_018: Render partner logo rail/marquee."""
import pytest
from pytest_bdd import scenarios

from tests.steps.emids_lp_018_partner_logo_rail_steps import *  # noqa: F401, F403

scenarios("../../tests/features/emids_lp_018_partner_logo_rail.feature")
