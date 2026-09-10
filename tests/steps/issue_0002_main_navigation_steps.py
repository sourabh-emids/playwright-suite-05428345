"""Step bindings for issue_0002 main navigation."""

from playwright.sync_api import Page
from pytest_bdd import given, parsers, then, when

from pages.issue_0002_main_navigation_page import MainNavigationPage


@given(
    "the Emids homepage is open for navigation",
    target_fixture="main_navigation_page",
)
def open_homepage(page: Page) -> MainNavigationPage:
    navigation_page = MainNavigationPage(page)
    navigation_page.open()
    return navigation_page


@when(parsers.parse('the user opens the "{menu}" main navigation menu'))
def open_navigation_menu(
    main_navigation_page: MainNavigationPage,
    menu: str,
) -> None:
    main_navigation_page.open_menu(menu)


@when(
    parsers.parse(
        'the user selects the "{destination}" destination for "{path}"'
    )
)
def select_navigation_destination(
    main_navigation_page: MainNavigationPage,
    destination: str,
    path: str,
) -> None:
    main_navigation_page.select_destination(destination, path)


@then(parsers.parse('the browser opens the navigation path "{path}"'))
def verify_navigation_path(
    main_navigation_page: MainNavigationPage,
    path: str,
) -> None:
    main_navigation_page.verify_path(path)
