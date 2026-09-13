"""Tests for Google Tag Manager container loading (issue_0037)."""
from tests.steps.issue_0037_gtm_loading_steps import *
from tests.steps.common_steps import *
from pytest_bdd import scenarios

scenarios("issue_0037_gtm_loading.feature")
