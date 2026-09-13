"""Test file for emids_lp_007-008: Connect CTA and Responsive Nav."""
import pytest
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.emids_lp_004_industries_steps import *  # noqa: F401, F403
from tests.steps.emids_lp_008_responsive_steps import *  # noqa: F401, F403

scenarios(
    "emids_lp_007_connect_cta.feature",
    "emids_lp_008_responsive_nav.feature",
)
