"""Test file for emids_lp_011: Optimize hero media loading."""
import pytest
from pytest_bdd import scenarios

from tests.steps.emids_lp_011_optimize_hero_media_steps import *  # noqa: F401, F403

scenarios("../../tests/features/emids_lp_011_optimize_hero_media.feature")
