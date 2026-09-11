"""Step definitions for TC-02 main navigation routing."""
from playwright.sync_api import Page
from pytest_bdd import given, parsers, then, when

from pages.tc_02_main_navigation_routing_page import Tc02MainNavigationRoutingPage


@given("the TC-02 user is on the Emids homepage")
def open_homepage(page: Page) -> None:
    Tc02MainNavigationRoutingPage(page).open_homepage()


@when(parsers.parse('the TC-02 user selects the "{menu_name}" main navigation category'))
def select_main_navigation_category(page: Page, menu_name: str) -> None:
    Tc02MainNavigationRoutingPage(page).select_menu_destination(menu_name)


@then(
    parsers.parse(
        'the TC-02 "{menu_name}" destination "{expected_path}" loads without an error'
    )
)
def navigation_destination_loads(
    page: Page, menu_name: str, expected_path: str
) -> None:
    Tc02MainNavigationRoutingPage(page).assert_destination_loaded(expected_path)
