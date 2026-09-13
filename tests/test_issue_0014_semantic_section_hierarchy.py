"""Test glue for issue_0014: Semantic section hierarchy"""

from pytest_bdd import scenarios

from tests.steps.issue_0014_semantic_section_hierarchy_steps import *
from tests.steps import common_steps

scenarios("issue_0014_semantic_section_hierarchy.feature")
