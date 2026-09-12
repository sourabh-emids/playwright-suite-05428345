from pytest_bdd import scenarios

from tests.steps.tc_01_homepage_loads_successfully_steps import *  # noqa: F401,F403

scenarios("tc_01_homepage_loads_successfully.feature")
