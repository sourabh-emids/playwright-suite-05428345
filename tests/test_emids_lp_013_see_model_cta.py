"""Test file for emids_lp_013: Provide See the model CTA."""
import pytest
from pytest_bdd import scenarios

from tests.steps.emids_lp_013_see_model_cta_steps import *  # noqa: F401, F403

scenarios("../../tests/features/emids_lp_013_see_model_cta.feature")
