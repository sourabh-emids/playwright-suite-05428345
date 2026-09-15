"""Tests for issue_0005: Contact form validates required fields."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0005_contact_form_validation_steps import *


scenarios("../features/issue_0005_contact_form_validation.feature")
