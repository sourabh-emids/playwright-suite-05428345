"""Step definitions for TC-03."""

from playwright.sync_api import Page
from pytest_bdd import given, then, when

from pages.tc_03_important_buttons_page import ImportantButtonsPage


@given("the homepage is loaded for calls to action")
def homepage_is_loaded_for_calls_to_action(page: Page) -> None:
    ImportantButtonsPage(page).load_homepage()


@when("the visitor selects the header Connect action")
def visitor_selects_header_connect(page: Page) -> None:
    ImportantButtonsPage(page).open_contact_from_header()


@then("the contact page opens successfully")
def contact_page_opens_successfully(page: Page) -> None:
    ImportantButtonsPage(page).assert_contact_page_open()


@when("the visitor selects Contact Us from the Company menu")
def visitor_selects_company_contact(page: Page) -> None:
    ImportantButtonsPage(page).open_contact_from_company_menu()


@when("the visitor selects the See How We Deliver Outcomes action")
def visitor_selects_outcomes_action(page: Page) -> None:
    ImportantButtonsPage(page).open_outcomes_cta()


@then("the outcomes page opens successfully")
def outcomes_page_opens_successfully(page: Page) -> None:
    ImportantButtonsPage(page).assert_outcomes_page_open()
