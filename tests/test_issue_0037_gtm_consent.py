"""Test runner for issue_0037: Load GTM with consent governance."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0037_gtm_consent_steps import *  # noqa: F401, F403

scenarios("issue_0037_gtm_consent.feature")
