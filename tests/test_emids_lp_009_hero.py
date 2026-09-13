"""Test file for emids_lp_009-013: Hero, How We Deliver, See the model CTA."""
import pytest
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.emids_lp_009_hero_steps import *  # noqa: F401, F403

scenarios(
    "emids_lp_009_hero.feature",
    "emids_lp_010_hero_cta_fdce.feature",
    "emids_lp_011_hero_media.feature",
    "emids_lp_012_how_we_deliver.feature",
    "emids_lp_013_see_model_cta.feature",
)
