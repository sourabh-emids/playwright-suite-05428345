"""Test file for emids_lp_002: Implement Solutions mega-menu."""
import pytest
from pytest_bdd import scenarios

from tests.steps.emids_lp_002_solutions_mega_menu_steps import *  # noqa: F401, F403

scenarios("../../tests/features/emids_lp_002_solutions_mega_menu.feature")
