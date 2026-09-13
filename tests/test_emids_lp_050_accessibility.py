"""Test file for emids_lp_050-055: Accessibility, SEO, Performance, Script Failures, Modal."""
import pytest
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.emids_lp_027_insights_cards_steps import *  # noqa: F401, F403

scenarios(
    "emids_lp_050_wcag_compliance.feature",
    "emids_lp_051_seo_metadata.feature",
    "emids_lp_052_responsive_layout.feature",
    "emids_lp_053_performance.feature",
    "emids_lp_054_script_failures.feature",
    "emids_lp_055_modal_behavior.feature",
)
