"""Test file for emids_lp_005: Implement Insights navigation group."""
import pytest
from pytest_bdd import scenarios

from tests.steps.emids_lp_005_insights_navigation_steps import *  # noqa: F401, F403

scenarios("../../tests/features/emids_lp_005_insights_navigation.feature")
