"""Test glue file for REQ-004: Website displays correctly on mobile viewport."""

from pytest_bdd import scenarios

from tests.steps.req_004_mobile_viewport_steps import *  # noqa: F401,F403

scenarios("req_004_mobile_viewport.feature")
