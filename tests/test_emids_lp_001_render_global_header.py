"""Test file for emids_lp_001: Render global header and Emids brand."""
import pytest
from pytest_bdd import scenarios

from tests.steps.emids_lp_001_render_global_header_steps import *  # noqa: F401, F403

scenarios("../../tests/features/emids_lp_001_render_global_header.feature")
