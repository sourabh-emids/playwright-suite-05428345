"""Test glue file for REQ-001: Homepage loads successfully."""

from pytest_bdd import scenarios

from tests.steps.req_001_homepage_load_steps import *  # noqa: F401,F403

scenarios("req_001_homepage_load.feature")
