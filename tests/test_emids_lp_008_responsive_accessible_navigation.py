"""Test file for emids_lp_008: Responsive accessible navigation behavior."""
import pytest
from pytest_bdd import scenarios

from tests.steps.emids_lp_008_responsive_accessible_navigation_steps import *  # noqa: F401, F403

scenarios("../../tests/features/emids_lp_008_responsive_accessible_navigation.feature")
