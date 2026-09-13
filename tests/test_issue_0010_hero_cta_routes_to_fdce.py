"""Test glue for issue_0010: Hero CTA routes to FDCE"""

from pytest_bdd import scenarios

from tests.steps.issue_0010_hero_cta_routes_to_fdce_steps import *
from tests.steps import common_steps

scenarios("issue_0010_hero_cta_routes_to_fdce.feature")
