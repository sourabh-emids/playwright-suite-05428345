"""Test file for emids_lp_010: Route hero CTA to FDCE experience."""
import pytest
from pytest_bdd import scenarios

from tests.steps.emids_lp_010_hero_cta_fdce_steps import *  # noqa: F401, F403

scenarios("../../tests/features/emids_lp_010_hero_cta_fdce.feature")
