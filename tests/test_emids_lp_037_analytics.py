"""Test file for emids_lp_037-044: Analytics and Media Integration."""
import pytest
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.emids_lp_027_insights_cards_steps import *  # noqa: F401, F403

scenarios(
    "emids_lp_037_gtm_consent.feature",
    "emids_lp_038_google_analytics.feature",
    "emids_lp_039_campaign_attribution.feature",
    "emids_lp_040_marketo_integration.feature",
    "emids_lp_041_linkedin_integration.feature",
    "emids_lp_042_zoominfo_integration.feature",
    "emids_lp_043_wistia_embeds.feature",
    "emids_lp_044_youtube_embeds.feature",
)
