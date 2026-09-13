"""Test file for emids_lp_036, 045-046: Footer sections."""
import pytest
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.emids_lp_027_insights_cards_steps import *  # noqa: F401, F403

scenarios(
    "emids_lp_036_cookie_preferences.feature",
    "emids_lp_045_footer_legal.feature",
    "emids_lp_046_footer_corporate.feature",
)
