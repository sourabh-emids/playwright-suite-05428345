"""Test runner for issue_0001: Render global header with Emids branding."""
import pytest
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0001_header_visibility_steps import *  # noqa: F401, F403

scenarios("issue_0001_header_visibility.feature")
