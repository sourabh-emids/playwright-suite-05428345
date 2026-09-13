"""Test file for emids_lp_034-035: Final CTA and Timing Message."""
import pytest
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.emids_lp_027_insights_cards_steps import *  # noqa: F401, F403

scenarios(
    "emids_lp_034_final_cta_banner.feature",
    "emids_lp_035_timing_message.feature",
)
