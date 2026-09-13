"""Test file for emids_lp_014-026: Semantic Hierarchy, Featured Solutions, Partnerships, Capabilities, Who We Serve, Impact, Insights."""
import pytest
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.emids_lp_014_global_steps import *  # noqa: F401, F403

scenarios(
    "emids_lp_014_semantic_hierarchy.feature",
    "emids_lp_015_featured_solutions.feature",
    "emids_lp_016_all_solutions_cta.feature",
    "emids_lp_017_responsive_solution.feature",
    "emids_lp_018_partner_logos.feature",
    "emids_lp_019_reduced_motion_partners.feature",
    "emids_lp_020_capabilities_overview.feature",
    "emids_lp_021_ai_capability.feature",
    "emids_lp_022_engineering_capability.feature",
    "emids_lp_023_platforms_capability.feature",
    "emids_lp_024_who_we_serve.feature",
    "emids_lp_025_impact_metrics.feature",
    "emids_lp_026_insights_section.feature",
)
