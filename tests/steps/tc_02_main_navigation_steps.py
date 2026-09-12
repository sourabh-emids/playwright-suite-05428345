"""Step definitions for TC-02."""

import re

from playwright.sync_api import Page, expect
from pytest_bdd import given, parsers, then, when

from pages.tc_02_main_navigation_page import MainNavigationPage


@given("the homepage is loaded for navigation")
def homepage_is_loaded_for_navigation(page: Page) -> None:
    MainNavigationPage(page).load()


@when(
    parsers.parse(
        'the visitor opens the "{menu}" menu and selects "{item}"'
    )
)
def visitor_selects_navigation_item(page: Page, menu: str, item: str) -> None:
    navigation = MainNavigationPage(page)
    expected = navigation.target_for(menu)
    assert expected["item"] == item
    navigation.open_expected_destination(menu)


@then(parsers.parse('the expected "{path}" page is open'))
def expected_navigation_page_is_open(page: Page, path: str) -> None:
    expect(page).to_have_url(re.compile(re.escape(path) + r"$"))
    expect(page.locator("main")).to_be_visible()
