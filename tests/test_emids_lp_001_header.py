"""Test file for emids_lp_001: Render global header and brand entry point."""
import pytest
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.emids_lp_001_header_steps import *  # noqa: F401, F403

scenarios("emids_lp_001_header.feature")
