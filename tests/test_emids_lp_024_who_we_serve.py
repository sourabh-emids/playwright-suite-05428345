"""Test file for emids_lp_024: Render five audience industry entries."""
import pytest
from pytest_bdd import scenarios

from tests.steps.emids_lp_024_who_we_serve_steps import *  # noqa: F401, F403

scenarios("../../tests/features/emids_lp_024_who_we_serve.feature")
