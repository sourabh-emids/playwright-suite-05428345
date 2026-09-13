"""Test file for emids_lp_027-033: Insight cards and Resource access."""
import pytest
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.emids_lp_027_insights_cards_steps import *  # noqa: F401, F403

scenarios(
    "emids_lp_027_medicare_ebook.feature",
    "emids_lp_028_cms0057_card.feature",
    "emids_lp_029_life_sciences_ebook.feature",
    "emids_lp_030_ai_roi_ebook.feature",
    "emids_lp_031_finops_payer_card.feature",
    "emids_lp_032_payer_blog_card.feature",
    "emids_lp_033_resource_access.feature",
)
