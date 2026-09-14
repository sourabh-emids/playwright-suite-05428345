"""Test runner for issue_0051: Implement SEO metadata and crawlable structure."""
from pytest_bdd import scenarios

from tests.steps import common_steps
from tests.steps.issue_0051_seo_metadata_steps import *  # noqa: F401, F403

scenarios("issue_0051_seo_metadata.feature")
