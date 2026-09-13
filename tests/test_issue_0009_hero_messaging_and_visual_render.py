"""Test glue for issue_0009: Hero messaging and visual render"""

from pytest_bdd import scenarios

from tests.steps.issue_0009_hero_messaging_and_visual_render_steps import *
from tests.steps import common_steps

scenarios("issue_0009_hero_messaging_and_visual_render.feature")
