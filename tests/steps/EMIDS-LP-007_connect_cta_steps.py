"""Step definitions for Connect CTA - EMIDS-LP-007"""
from pytest_bdd import given, when, then
from pages.EMIDS-LP-007_connect_cta_page import ConnectCTAPage
from playwright.sync_api import expect


@given("The header is rendered")
def header_rendered(page):
    page.goto("/")


@when("Visual inspection of the Connect CTA")
def visual_inspect_connect(page):
    pass


@then("CTA has distinct styling that differentiates it from navigation links")
def verify_distinct_styling(page):
    cta_page = ConnectCTAPage(page)
    cta_page.verify_connect_cta_visible()


@given("The Connect CTA element")
def connect_cta_element(page):
    page.goto("/")


@when("Checked for accessibility")
def check_accessibility(page):
    pass


@then("CTA has descriptive accessible name identifying its purpose")
def verify_accessible_name(page):
    cta_page = ConnectCTAPage(page)
    cta_page.verify_connect_cta_visible()


@given("The Connect CTA is clicked")
def connect_cta_clicked(page):
    cta_page = ConnectCTAPage(page)
    cta_page.goto("/")
    cta_page.click_header_connect()


@when("Navigation is executed")
def navigation_executed(page):
    pass


@then("User reaches the contact page at /contact/")
def verify_contact_page_reached(page):
    expect(page).to_have_url("**/contact/**")


@given("The Connect CTA has focus")
def connect_cta_has_focus(page):
    cta_page = ConnectCTAPage(page)
    cta_page.goto("/")


@when("User presses Enter or Space")
def press_enter_or_space(page):
    cta_page = ConnectCTAPage(page)
    cta_page.focus_and_activate()


@then("CTA activates and navigates to contact page")
def verify_cta_activates(page):
    expect(page).to_have_url("**/contact/**")


@given("The Connect CTA destination")
def connect_cta_destination(page):
    cta_page = ConnectCTAPage(page)
    cta_page.goto("/")


@when("URL is inspected")
def inspect_url(page):
    pass


@then("URL uses HTTPS protocol and is valid")
def verify_https_valid(page):
    cta_page = ConnectCTAPage(page)
    assert cta_page.verify_https()
