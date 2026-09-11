"""Step definitions for TC-03 primary call-to-action navigation."""
from playwright.sync_api import Page
from pytest_bdd import given, parsers, then, when

from pages.tc_03_primary_cta_navigation_page import Tc03PrimaryCtaNavigationPage


@given("the TC-03 user is on the Emids homepage")
def open_homepage(page: Page) -> None:
    Tc03PrimaryCtaNavigationPage(page).open_homepage()


@when(parsers.parse('the TC-03 user selects the "{cta_name}" primary call to action'))
def select_primary_cta(page: Page, cta_name: str) -> None:
    Tc03PrimaryCtaNavigationPage(page).select_cta(cta_name)


@then(
    parsers.parse(
        'the TC-03 "{cta_name}" destination "{expected_path}" loads without an error'
    )
)
def cta_destination_loads(page: Page, cta_name: str, expected_path: str) -> None:
    Tc03PrimaryCtaNavigationPage(page).assert_destination_loaded(expected_path)
