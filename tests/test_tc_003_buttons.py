"""Test file for tc_003 - Main buttons functionality and navigation."""
import pytest
from pytest_bdd import scenarios

from tests.steps.tc_003_buttons_steps import *
from tests.steps.common_steps import *


scenarios("tc_003_buttons.feature")
