from playwright.sync_api import Page
from pytest_bdd import given, parsers, then, when

from pages.issue_0002_navigation_page import Issue0002NavigationPage


@given(
    "the Emids homepage and main navigation are available",
    target_fixture="navigation_page",
)
def homepage_with_navigation(page: Page) -> Issue0002NavigationPage:
    navigation_page = Issue0002NavigationPage(page)
    navigation_page.open()
    return navigation_page


@when(
    parsers.parse(
        'the user opens the "{navigation_item}" menu and selects its '
        '"{destination}" destination'
    )
)
def select_navigation_destination(
    navigation_page: Issue0002NavigationPage,
    navigation_item: str,
    destination: str,
) -> None:
    navigation_page.select_navigation_destination(
        navigation_item,
        destination,
    )


@then(parsers.parse('the intended "{path}" page opens'))
def verify_navigation_destination(
    navigation_page: Issue0002NavigationPage,
    path: str,
) -> None:
    navigation_page.assert_destination_opened(path)
