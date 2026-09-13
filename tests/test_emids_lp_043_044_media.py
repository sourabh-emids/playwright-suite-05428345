"""Test file for emids_lp_043-044: Media embeds conditional."""
import pytest
from pytest_bdd import scenarios

from tests.steps.emids_lp_043_044_media_steps import *  # noqa: F401, F403

scenarios("../../tests/features/emids_lp_043_044_media.feature")
