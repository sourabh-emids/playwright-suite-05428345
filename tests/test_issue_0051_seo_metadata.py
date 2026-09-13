"""Tests for SEO metadata and crawlable structure (issue_0051)."""
from tests.steps.issue_0051_seo_metadata_steps import *
from tests.steps.common_steps import *
from pytest_bdd import scenarios

scenarios("issue_0051_seo_metadata.feature")
