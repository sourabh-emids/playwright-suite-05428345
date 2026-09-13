"""Test glue for issue_0026: Insights section and cards render"""

from pytest_bdd import scenarios

from tests.steps.issue_0026_insights_section_and_cards_render_steps import *
from tests.steps import common_steps

scenarios("issue_0026_insights_section_and_cards_render.feature")
