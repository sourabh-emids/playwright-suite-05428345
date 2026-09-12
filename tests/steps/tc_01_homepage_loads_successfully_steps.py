"""Step definitions for TC-01."""

from playwright.sync_api import Page
from pytest_bdd import given, parsers, then, when

from pages.tc_01_homepage_loads_successfully_page import HomepageAvailabilityPage


@given("the homepage is available")
def homepage_is_available(page: Page) -> None:
    HomepageAvailabilityPage(page).load()


@when("the visitor opens the Emids homepage")
def visitor_opens_homepage(page: Page) -> None:
    HomepageAvailabilityPage(page).load()


@then("the homepage is loaded and usable")
def homepage_is_loaded_and_usable(page: Page) -> None:
    HomepageAvailabilityPage(page).assert_loaded()


@then("no obvious error is displayed")
def no_obvious_error_is_displayed(page: Page) -> None:
    body_text = HomepageAvailabilityPage(page).visible_error_text()
    forbidden_messages = (
        "404 not found",
        "internal server error",
        "application error",
    )
    assert not any(message in body_text for message in forbidden_messages)
