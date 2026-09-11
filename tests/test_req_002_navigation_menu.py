"""Test glue file for REQ-002: Main navigation menu items navigate to correct pages."""

from pytest_bdd import scenarios

from tests.steps.req_002_navigation_menu_steps import *  # noqa: F401,F403

scenarios("req_002_navigation_menu.feature")
