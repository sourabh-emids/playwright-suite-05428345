"""Step definitions for the Emids public website feature suite."""
import pytest
from playwright.sync_api import Page
from pytest_bdd import given, parsers, scenarios, then, when

from pages.emids_page import EmidsPage


scenarios(
    "../features/tc_01_homepage.feature",
    "../features/tc_02_main_navigation.feature",
    "../features/tc_03_calls_to_action.feature",
    "../features/tc_04_mobile_view.feature",
    "../features/tc_05_contact_validation.feature",
)


@pytest.fixture
def emids_page(page: Page) -> EmidsPage:
    return EmidsPage(page)


@given("the Emids homepage is open")
def emids_homepage_is_open(emids_page: EmidsPage) -> None:
    emids_page.open_home()


@when("the user opens the Emids homepage")
def user_opens_homepage(emids_page: EmidsPage) -> None:
    emids_page.open_home()


@then("the homepage loads successfully without obvious errors")
def homepage_loads_without_errors(emids_page: EmidsPage) -> None:
    emids_page.assert_homepage_loaded_without_obvious_errors()


@when(parsers.parse('the user opens the "{menu}" menu and selects "{item}"'))
def open_navigation_destination(emids_page: EmidsPage, menu: str, item: str) -> None:
    emids_page.open_navigation_destination(menu, item)


@then(parsers.parse('the destination path is "{path}"'))
def destination_path_is(emids_page: EmidsPage, path: str) -> None:
    emids_page.assert_path_opened(path)


@when("the user selects Contact Us from the Company menu")
def select_contact_us(emids_page: EmidsPage) -> None:
    emids_page.open_contact_from_company_menu()


@then("the Emids contact page opens")
def contact_page_opens(emids_page: EmidsPage) -> None:
    emids_page.assert_contact_page_opened()


@given("the Emids partners page is open")
def partners_page_is_open(emids_page: EmidsPage) -> None:
    emids_page.open_partners_page()


@when("the user selects Learn More for Snowflake")
def select_snowflake_learn_more(emids_page: EmidsPage) -> None:
    emids_page.open_snowflake_with_learn_more()


@then("the Snowflake partner page opens")
def snowflake_partner_page_opens(emids_page: EmidsPage) -> None:
    emids_page.assert_snowflake_partner_page_opened()


@given("the browser uses a 390 by 844 mobile viewport")
def use_mobile_viewport(emids_page: EmidsPage) -> None:
    emids_page.use_mobile_viewport()


@then("the main mobile text, image, menu control, and call-to-action are visible")
def mobile_content_is_visible(emids_page: EmidsPage) -> None:
    emids_page.assert_mobile_home_content_visible()


@when("the user opens the mobile menu")
def open_mobile_menu(emids_page: EmidsPage) -> None:
    emids_page.open_mobile_menu()


@then("the mobile navigation is visible and usable")
def mobile_navigation_is_usable(emids_page: EmidsPage) -> None:
    emids_page.use_mobile_connect_link()
    emids_page.assert_contact_page_opened()


@given("the contact form is open with all required fields empty")
def empty_contact_form_is_open(emids_page: EmidsPage) -> None:
    emids_page.open_contact_form()
    emids_page.assert_required_fields_are_empty()


@when("the user submits the empty contact form")
def submit_empty_contact_form(emids_page: EmidsPage) -> None:
    emids_page.submit_contact_form()


@then("a clear required-field validation message is displayed")
def required_validation_is_displayed(emids_page: EmidsPage) -> None:
    emids_page.assert_required_validation_is_clear()
