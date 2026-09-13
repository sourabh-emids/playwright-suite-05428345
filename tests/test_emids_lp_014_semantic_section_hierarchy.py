"""Test file for emids_lp_014: Maintain semantic section hierarchy."""
import pytest
from pytest_bdd import scenarios

from tests.steps.emids_lp_014_semantic_section_hierarchy_steps import *  # noqa: F401, F403

scenarios("../../tests/features/emids_lp_014_semantic_section_hierarchy.feature")
