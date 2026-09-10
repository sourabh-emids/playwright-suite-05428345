from pytest_bdd import scenarios

from tests.steps.issue_0001_website_homepage_steps import *  # noqa: F401,F403

scenarios("issue_0001_website_homepage.feature")
