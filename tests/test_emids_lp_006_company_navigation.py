"""Test file for emids_lp_006: Implement Company navigation group."""
import pytest
from pytest_bdd import scenarios

from tests.steps.emids_lp_006_company_navigation_steps import *  # noqa: F401, F403

scenarios("../../tests/features/emids_lp_006_company_navigation.feature")
