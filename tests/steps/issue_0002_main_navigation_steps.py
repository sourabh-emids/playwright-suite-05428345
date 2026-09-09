"""Step definitions for issue_0002 main navigation."""

from playwright.sync_api import Page
from pytest_bdd import given, parsers, then, when

from pages.issue_0002_main_navigation_page import MainNavigationPage


@given(
    "the homepage main navigation is available",
    target_fixture="navigation_page",
)
def open_navigation_page(page: Page) -> MainNavigationPage:
    navigation_page = MainNavigationPage(page)
    navigation_page.open()
    return navigation_page


@when(
    parsers.parse(
        'the user opens the "{menu}" menu and selects "{destination}"'
    )
)
def select_menu_destination(
    navigation_page: MainNavigationPage,
    menu: str,
    destination: str,
) -> None:
    navigation_page.select_menu_destination(menu, destination)


@when("the user selects Connect from the header")
def select_connect(navigation_page: MainNavigationPage) -> None:
    navigation_page.select_connect()


@then(
    parsers.parse(
        'the destination path is "{path}" with heading "{heading}"'
    )
)
def verify_destination(
    navigation_page: MainNavigationPage,
    path: str,
    heading: str,
) -> None:
    navigation_page.assert_destination(path, heading)
