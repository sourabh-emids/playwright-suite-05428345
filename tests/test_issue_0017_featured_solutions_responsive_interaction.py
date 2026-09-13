"""Test glue for issue_0017: Featured solutions responsive interaction"""

from pytest_bdd import scenarios

from tests.steps.issue_0017_featured_solutions_responsive_interaction_steps import *
from tests.steps import common_steps

scenarios("issue_0017_featured_solutions_responsive_interaction.feature")
