"""Tests for Semantic section hierarchy (issue_0014)."""
from tests.steps.issue_0014_semantic_hierarchy_steps import *
from tests.steps.common_steps import *
from pytest_bdd import scenarios

scenarios("issue_0014_semantic_hierarchy.feature")
