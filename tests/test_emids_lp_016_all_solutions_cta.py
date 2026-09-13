"""Test file for emids_lp_016: Provide All Solutions CTA."""
import pytest
from pytest_bdd import scenarios

from tests.steps.emids_lp_016_all_solutions_cta_steps import *  # noqa: F401, F403

scenarios("../../tests/features/emids_lp_016_all_solutions_cta.feature")
