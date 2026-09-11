"""Test glue file for REQ-003: Primary CTA buttons function correctly."""

from pytest_bdd import scenarios

from tests.steps.req_003_cta_buttons_steps import *  # noqa: F401,F403

scenarios("req_003_cta_buttons.feature")
