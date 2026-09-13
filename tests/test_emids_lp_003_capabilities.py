"""Test file for emids_lp_003: Implement Capabilities mega-menu."""
import pytest
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.emids_lp_003_capabilities_steps import *  # noqa: F401, F403

scenarios("emids_lp_003_capabilities_menu.feature")
