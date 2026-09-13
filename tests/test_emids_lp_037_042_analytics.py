"""Test file for emids_lp_037-042: Analytics and marketing integration."""
import pytest
from pytest_bdd import scenarios

from tests.steps.emids_lp_037_042_analytics_steps import *  # noqa: F401, F403

scenarios("../../tests/features/emids_lp_037_042_analytics.feature")
