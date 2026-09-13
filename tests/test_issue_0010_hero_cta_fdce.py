"""Tests for Hero CTA routes to FDCE experience (issue_0010)."""
from tests.steps.issue_0010_hero_cta_fdce_steps import *
from tests.steps.common_steps import *
from pytest_bdd import scenarios

scenarios("issue_0010_hero_cta_fdce.feature")
