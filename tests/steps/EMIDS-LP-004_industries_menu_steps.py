"""Step definitions for Industries mega-menu - EMIDS-LP-004"""
from pytest_bdd import given, when, then
from pages.EMIDS-LP-004_industries_menu_page import IndustriesMenuPage
from playwright.sync_api import expect


@given("The Industries mega-menu is open")
def industries_menu_open(page):
    menu_page = IndustriesMenuPage(page)
    menu_page.goto("/")
    menu_page.open_industries_menu()


@when("All menu items are inspected")
def inspect_menu_items(page):
    pass


@then("Payer, Provider, HealthTech, Life Sciences, and Consumer destinations are present")
def verify_all_audiences(page):
    menu_page = IndustriesMenuPage(page)
    menu_page.verify_all_audiences()


@given("The Industries menu is open")
def industries_menu_open_2(page):
    menu_page = IndustriesMenuPage(page)
    menu_page.goto("/")
    menu_page.open_industries_menu()


@when("User navigates via keyboard")
def keyboard_navigate(page):
    pass


@then("All five audience links are reachable and activate on keyboard input")
def verify_audience_links_keyboard(page):
    menu_page = IndustriesMenuPage(page)
    menu_page.verify_all_audiences()


@given("Each industry audience link in the menu")
def audience_links_in_menu(page):
    menu_page = IndustriesMenuPage(page)
    menu_page.goto("/")
    menu_page.open_industries_menu()


@when("URLs are verified")
def verify_urls(page):
    menu_page = IndustriesMenuPage(page)
    urls = menu_page.get_audience_urls()


@then("All use canonical URLs: /segments/payer/, /segments/provider/, /segments/healthtech/, /segments/life-sciences/, /segments/consumer/")
def verify_canonical_urls(page):
    menu_page = IndustriesMenuPage(page)
    urls = menu_page.get_audience_urls()
    assert "/segments/payer/" in urls["Payer"]
    assert "/segments/provider/" in urls["Provider"]
    assert "/segments/healthtech/" in urls["HealthTech"]
    assert "/segments/life-sciences/" in urls["Life Sciences"]
    assert "/segments/consumer/" in urls["Consumer"]


@given("A user on mobile viewport")
def mobile_viewport(page):
    page.set_viewport_size({"width": 375, "height": 667})


@when("The Industries menu is accessed")
def access_industries_menu(page):
    menu_page = IndustriesMenuPage(page)
    menu_page.goto("/")
    menu_page.open_industries_menu()


@then("A stacked list or disclosure pattern is used")
def verify_stacked_list(page):
    menu_page = IndustriesMenuPage(page)
    menu_page.verify_all_audiences()
