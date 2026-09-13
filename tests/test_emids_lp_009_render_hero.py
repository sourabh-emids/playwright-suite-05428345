"""Test file for emids_lp_009: Render hero messaging and visual."""
import pytest
from pytest_bdd import scenarios

from tests.steps.emids_lp_009_render_hero_steps import *  # noqa: F401, F403

scenarios("../../tests/features/emids_lp_009_render_hero.feature")
