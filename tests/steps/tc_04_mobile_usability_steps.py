"""Step definitions for TC-04."""

from playwright.sync_api import Page
from pytest_bdd import given, then, when

from pages.tc_04_mobile_usability_page import MobileUsabilityPage


@given("the homepage is opened in a mobile-sized browser")
def homepage_is_opened_in_mobile_browser(page: Page) -> None:
    mobile = MobileUsabilityPage(page)
    mobile.set_mobile_viewport()
    mobile.load()


@when("the visitor views the mobile homepage")
def visitor_views_mobile_homepage(page: Page) -> None:
    MobileUsabilityPage(page).assert_core_content_visible()


@then("the mobile hero content and controls are visible")
def mobile_hero_content_is_visible(page: Page) -> None:
    MobileUsabilityPage(page).assert_core_content_visible()


@when("the visitor opens the mobile menu")
def visitor_opens_mobile_menu(page: Page) -> None:
    MobileUsabilityPage(page).open_mobile_menu()


@then("the mobile navigation control is usable")
def mobile_navigation_control_is_usable(page: Page) -> None:
    MobileUsabilityPage(page).assert_menu_control_usable()
