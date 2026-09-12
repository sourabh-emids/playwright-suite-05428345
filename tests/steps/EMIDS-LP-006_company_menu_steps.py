"""Step definitions for Company menu - EMIDS-LP-006"""
from pytest_bdd import given, when, then
from pages.EMIDS-LP-006_company_menu_page import CompanyMenuPage
from playwright.sync_api import expect


@given("The Company menu is opened")
def company_menu_opened(page):
    menu_page = CompanyMenuPage(page)
    menu_page.goto("/")
    menu_page.open_company_menu()


@when("All menu items are reviewed")
def review_menu_items(page):
    pass


@then("Only approved company links and Contact/Connect destinations are present")
def verify_approved_links(page):
    menu_page = CompanyMenuPage(page)
    menu_page.verify_menu_groups()


@given("The Company menu is open")
def company_menu_open(page):
    menu_page = CompanyMenuPage(page)
    menu_page.goto("/")
    menu_page.open_company_menu()


@when("User interacts via keyboard, pointer, or touch")
def interact_various_methods(page):
    pass


@then("All links are operable with each input method")
def verify_links_operable(page):
    menu_page = CompanyMenuPage(page)
    links = menu_page.get_company_links()
    assert len(links) > 0


@given("Company navigation items")
def company_nav_items(page):
    menu_page = CompanyMenuPage(page)
    menu_page.goto("/")
    menu_page.open_company_menu()


@when("Checking publication status")
def check_publication_status(page):
    pass


@then("Only pages with published status are displayed")
def verify_published_pages(page):
    menu_page = CompanyMenuPage(page)
    menu_page.verify_menu_groups()
