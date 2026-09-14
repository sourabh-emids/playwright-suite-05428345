"""Test file for tc_002 - Main navigation menu items functionality."""
import pytest
from pytest_bdd import scenarios

from tests.steps.tc_002_navigation_steps import *
from tests.steps.common_steps import *


scenarios("tc_002_navigation.feature")
