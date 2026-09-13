"""Test file for emids_lp_026-033: Insights section and content cards."""
import pytest
from pytest_bdd import scenarios

from tests.steps.emids_lp_026_033_insights_section_steps import *  # noqa: F401, F403

scenarios("../../tests/features/emids_lp_026_033_insights_section.feature")
