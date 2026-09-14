"""Test file for tc_005 - Contact form validation messages."""
import pytest
from pytest_bdd import scenarios

from tests.steps.tc_005_form_validation_steps import *
from tests.steps.common_steps import *


scenarios("tc_005_form_validation.feature")
