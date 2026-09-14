"""Test file for tc_001 - Website homepage loads successfully."""
import pytest
from pytest_bdd import scenarios

from tests.steps.tc_001_homepage_steps import *
from tests.steps.common_steps import *


scenarios("tc_001_homepage.feature")
