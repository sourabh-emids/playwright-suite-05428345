"""Test file for emids_lp_047-049: Contact form functionality."""
import pytest
from pytest_bdd import scenarios

from tests.steps.emids_lp_047_048_049_contact_form_steps import *  # noqa: F401, F403

scenarios("../../tests/features/emids_lp_047_048_049_contact_form.feature")
