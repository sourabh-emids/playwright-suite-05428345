"""Step definitions for TC-04 mobile usability."""
from playwright.sync_api import Page
from pytest_bdd import given, then, when

from pages.tc_04_mobile_website_usability_page import Tc04MobileWebsiteUsabilityPage


@given("the TC-04 user opens the homepage in a mobile-sized browser window")
def open_mobile_homepage(page: Page) -> None:
    Tc04MobileWebsiteUsabilityPage(page).open_in_mobile_view()


@then("the TC-04 essential homepage content and controls are usable")
def initial_mobile_content_is_usable(page: Page) -> None:
    Tc04MobileWebsiteUsabilityPage(page).assert_initial_content_is_usable()


@when("the TC-04 user opens the mobile navigation menu")
def open_mobile_menu(page: Page) -> None:
    Tc04MobileWebsiteUsabilityPage(page).open_mobile_menu()


@then("the TC-04 mobile navigation and its primary button are usable")
def mobile_menu_controls_are_usable(page: Page) -> None:
    Tc04MobileWebsiteUsabilityPage(page).assert_mobile_menu_controls_are_usable()
