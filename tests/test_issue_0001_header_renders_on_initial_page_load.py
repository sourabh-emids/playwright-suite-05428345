"""Test glue for issue_0001: Render global header with navigation"""

from pytest_bdd import scenarios

from tests.steps.issue_0001_header_renders_on_initial_page_load_steps import *
from tests.steps import common_steps

scenarios("issue_0001_header_renders_on_initial_page_load.feature")
