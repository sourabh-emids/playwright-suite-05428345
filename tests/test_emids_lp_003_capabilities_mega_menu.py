"""Test file for emids_lp_003: Implement Capabilities mega-menu."""
import pytest
from pytest_bdd import scenarios

from tests.steps.emids_lp_003_capabilities_mega_menu_steps import *  # noqa: F401, F403

scenarios("../../tests/features/emids_lp_003_capabilities_mega_menu.feature")
