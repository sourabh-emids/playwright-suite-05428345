"""Test file for tc_004 - Mobile responsive view functionality."""
import pytest
from pytest_bdd import scenarios

from tests.steps.tc_004_mobile_steps import *
from tests.steps.common_steps import *


scenarios("tc_004_mobile.feature")
