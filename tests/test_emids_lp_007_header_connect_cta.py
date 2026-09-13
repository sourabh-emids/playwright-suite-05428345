"""Test file for emids_lp_007: Provide header Connect CTA."""
import pytest
from pytest_bdd import scenarios

from tests.steps.emids_lp_007_header_connect_cta_steps import *  # noqa: F401, F403

scenarios("../../tests/features/emids_lp_007_header_connect_cta.feature")
