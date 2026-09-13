"""Test file for emids_lp_005: Implement Insights navigation group."""
import pytest
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.emids_lp_004_industries_steps import *  # noqa: F401, F403

scenarios("emids_lp_005_insights_nav.feature")
