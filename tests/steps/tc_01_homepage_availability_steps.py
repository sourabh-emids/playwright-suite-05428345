"""Step definitions for TC-01 homepage availability."""
from playwright.sync_api import Page
from pytest_bdd import given, then

from pages.tc_01_homepage_availability_page import Tc01HomepageAvailabilityPage


@given("the TC-01 user opens the Emids homepage")
def open_homepage(page: Page) -> None:
    Tc01HomepageAvailabilityPage(page).open()


@then("the TC-01 homepage is loaded without an obvious error")
def homepage_loaded_without_error(page: Page) -> None:
    Tc01HomepageAvailabilityPage(page).assert_loaded_without_obvious_error()
