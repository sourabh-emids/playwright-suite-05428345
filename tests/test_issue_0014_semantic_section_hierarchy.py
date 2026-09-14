"""Test runner for issue_0014: Semantic Section Hierarchy."""
from pytest_bdd import scenarios
from tests.steps.issue_0014_semantic_section_hierarchy_steps import *
from tests.steps.common_steps import *

scenarios("issue_0014_semantic_section_hierarchy.feature")
