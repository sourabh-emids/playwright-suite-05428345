"""Test file for emids_lp_012: Render How We Deliver section."""
import pytest
from pytest_bdd import scenarios

from tests.steps.emids_lp_012_how_we_deliver_steps import *  # noqa: F401, F403

scenarios("../../tests/features/emids_lp_012_how_we_deliver.feature")
