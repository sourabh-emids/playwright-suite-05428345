import pytest
from playwright.sync_api import Page
from pytest_bdd import given, parsers, then, when

from pages.tc_02_main_navigation_page import Tc02MainNavigationPage


@pytest.fixture
def tc_02_navigation(page: Page) -> Tc02MainNavigationPage:
    return Tc02MainNavigationPage(page)


@given("the Emids homepage and main navigation are available")
def open_homepage(tc_02_navigation: Tc02MainNavigationPage) -> None:
    tc_02_navigation.open()


@when(
    parsers.parse(
        'I select the "{menu}" menu and its destination at "{path}"'
    )
)
def select_navigation_destination(
    tc_02_navigation: Tc02MainNavigationPage,
    menu: str,
    path: str,
) -> None:
    tc_02_navigation.select_destination(menu, path)


@then(
    parsers.parse(
        'the navigation destination "{path}" loads without a visible '
        "page error"
    )
)
def verify_navigation_destination(
    tc_02_navigation: Tc02MainNavigationPage,
    path: str,
) -> None:
    tc_02_navigation.assert_destination_loaded(path)
