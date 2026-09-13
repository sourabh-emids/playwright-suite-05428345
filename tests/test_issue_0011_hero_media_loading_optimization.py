"""Test glue for issue_0011: Hero media loading optimization"""

from pytest_bdd import scenarios

from tests.steps.issue_0011_hero_media_loading_optimization_steps import *
from tests.steps import common_steps

scenarios("issue_0011_hero_media_loading_optimization.feature")
