"""Test file for emids_lp_004: Implement Industries mega-menu."""
import pytest
from pytest_bdd import scenarios

from tests.steps.emids_lp_004_industries_mega_menu_steps import *  # noqa: F401, F403

scenarios("../../tests/features/emids_lp_004_industries_mega_menu.feature")
