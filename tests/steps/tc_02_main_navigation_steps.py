"""Step bindings for TC-02 desktop main navigation."""

import pytest
from playwright.sync_api import Page
from pytest_bdd import given, parsers, then, when

from pages.tc_02_main_navigation_page import MainNavigationPage


@pytest.fixture
def main_navigation(page: Page) -> MainNavigationPage:
    return MainNavigationPage(page)


@given("the Emids desktop main navigation is available")
def open_homepage(main_navigation: MainNavigationPage) -> None:
    main_navigation.open_homepage()


@when(
    parsers.parse(
        'I open the "{destination}" destination from the "{menu}" main '
        "navigation menu"
    )
)
def open_destination(
    main_navigation: MainNavigationPage,
    destination: str,
    menu: str,
) -> None:
    main_navigation.select_destination(menu, destination)


@then(
    parsers.parse(
        'the "{heading}" destination page for "{destination}" is displayed'
    )
)
def verify_destination(
    main_navigation: MainNavigationPage,
    heading: str,
    destination: str,
) -> None:
    main_navigation.assert_destination(destination, heading)
