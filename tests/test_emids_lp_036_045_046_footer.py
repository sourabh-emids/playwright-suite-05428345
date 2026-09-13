"""Test file for emids_lp_036, 045-046: Footer and cookie preferences."""
import pytest
from pytest_bdd import scenarios

from tests.steps.emids_lp_036_045_046_footer_steps import *  # noqa: F401, F403

scenarios("../../tests/features/emids_lp_036_footer_cookie.feature")
scenarios("../../tests/features/emids_lp_045_046_footer_legal.feature")
