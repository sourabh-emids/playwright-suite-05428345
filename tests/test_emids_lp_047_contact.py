"""Test file for emids_lp_047-049: Contact Form."""
import pytest
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.emids_lp_027_insights_cards_steps import *  # noqa: F401, F403

scenarios(
    "emids_lp_047_contact_form.feature",
    "emids_lp_048_inquiry_type.feature",
    "emids_lp_049_form_feedback.feature",
)
