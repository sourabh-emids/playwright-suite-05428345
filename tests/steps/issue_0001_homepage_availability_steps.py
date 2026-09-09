"""Step definitions for issue_0001 homepage availability."""

from playwright.sync_api import Page
from pytest_bdd import given, then

from pages.issue_0001_homepage_availability_page import (
    HomepageAvailabilityPage,
)


@given("the public homepage is open", target_fixture="homepage")
def open_homepage(page: Page) -> HomepageAvailabilityPage:
    homepage = HomepageAvailabilityPage(page)
    homepage.open()
    return homepage


@then("the homepage primary content is displayed without an error page")
def verify_homepage(homepage: HomepageAvailabilityPage) -> None:
    homepage.assert_loaded()
