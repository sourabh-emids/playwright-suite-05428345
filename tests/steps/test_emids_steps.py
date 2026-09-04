"""pytest-bdd bindings for the Emids public website requirements."""

import pytest
from playwright.sync_api import Page
from pytest_bdd import given, parsers, scenarios, then, when

from pages.contact_page import ContactPage
from pages.emids_site_page import EmidsSitePage


scenarios(
    "tc_01_homepage.feature",
    "tc_02_main_navigation.feature",
    "tc_03_primary_ctas.feature",
    "tc_04_mobile_experience.feature",
    "tc_05_contact_validation.feature",
)


@pytest.fixture
def emids_site(page: Page) -> EmidsSitePage:
    return EmidsSitePage(page)


@pytest.fixture
def contact_page(page: Page) -> ContactPage:
    return ContactPage(page)


@given("the user opens the Emids homepage")
def open_emids_homepage(emids_site: EmidsSitePage) -> None:
    emids_site.open_home()


@given("the Emids homepage is open in a desktop browser")
def open_desktop_homepage(emids_site: EmidsSitePage) -> None:
    emids_site.open_home()


@given("the Emids homepage is open at a 390 by 844 mobile viewport")
def open_mobile_homepage(emids_site: EmidsSitePage) -> None:
    emids_site.use_mobile_viewport()
    emids_site.open_home()


@given("the contact form is open with every required field empty")
def open_empty_contact_form(contact_page: ContactPage) -> None:
    contact_page.open()
    contact_page.verify_all_required_fields_are_empty()


@when(
    parsers.parse(
        'the user opens the "{navigation_item}" menu and selects its defined destination'
    )
)
def select_main_navigation_destination(
    emids_site: EmidsSitePage, navigation_item: str, expected_path: str
) -> None:
    emids_site.open_defined_navigation_destination(navigation_item, expected_path)


@when("the user selects Contact Us from the Company menu")
def select_contact_us(emids_site: EmidsSitePage) -> None:
    emids_site.select_contact_us()


@when("the user selects the homepage primary call to action")
def select_homepage_primary_cta(emids_site: EmidsSitePage) -> None:
    emids_site.select_primary_home_cta()


@when("the user opens the mobile menu and the Solutions section")
def open_mobile_solutions_menu(emids_site: EmidsSitePage) -> None:
    emids_site.open_mobile_solutions_menu()


@when("the user selects the mobile homepage primary call to action")
def select_mobile_primary_cta(emids_site: EmidsSitePage) -> None:
    emids_site.select_primary_home_cta()


@when("the user submits the empty contact form")
def submit_empty_contact_form(contact_page: ContactPage) -> None:
    contact_page.submit_empty_form()


@then("the homepage loads successfully")
def verify_homepage_loaded(emids_site: EmidsSitePage) -> None:
    emids_site.verify_home_loaded()


@then("no obvious error page is displayed")
def verify_no_obvious_error(emids_site: EmidsSitePage) -> None:
    emids_site.verify_no_obvious_error()


@then(parsers.parse('the corresponding page at "{expected_path}" opens'))
def verify_corresponding_page(
    emids_site: EmidsSitePage, expected_path: str
) -> None:
    emids_site.verify_destination_opened(expected_path)


@then("the Emids contact page opens")
def verify_contact_page(emids_site: EmidsSitePage) -> None:
    emids_site.verify_contact_page_opened()


@then("the Forward Deployed Context Engineering page opens")
def verify_primary_cta_destination(emids_site: EmidsSitePage) -> None:
    emids_site.verify_primary_cta_destination()


@then("the homepage text and logo are visible without horizontal overflow")
def verify_mobile_content(emids_site: EmidsSitePage) -> None:
    emids_site.verify_mobile_content()


@then("the mobile Solutions menu is visible and usable")
def verify_mobile_menu(emids_site: EmidsSitePage) -> None:
    emids_site.verify_mobile_solutions_menu()


@then(
    "every required contact field is identified and a clear validation message is displayed"
)
def verify_contact_validation(contact_page: ContactPage) -> None:
    contact_page.verify_required_field_validation()
