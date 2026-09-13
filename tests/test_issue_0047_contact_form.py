"""Tests for Contact form reached by Connect CTAs (issue_0047)."""
from tests.steps.issue_0047_contact_form_steps import *
from tests.steps.common_steps import *
from pytest_bdd import scenarios

scenarios("issue_0047_contact_form.feature")
