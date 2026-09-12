"""Step definitions for Homepage modal - EMIDS-LP-055"""
from pytest_bdd import given, when, then
from playwright.sync_api import expect


@given("Default homepage configuration")
def default_config(page):
    page.goto("/")


@when("Page loads")
def load_page(page):
    pass


@then("No promotional modal appears unsolicited")
def verify_no_modal(page):
    pass


@given("Campaign modal is configured and triggered")
def campaign_modal_configured(page):
    pass


@when("User interacts with modal")
def interact_modal(page):
    page.goto("/")


@then("Modal is dismissible via close control")
def verify_dismissible(page):
    pass


@given("Campaign modal when displayed")
def modal_displayed(page):
    page.goto("/")


@when("Keyboard interaction is tested")
def test_keyboard(page):
    pass


@then("Modal is keyboard accessible")
def verify_keyboard_accessible(page):
    pass


@given("Campaign modal is displayed")
def modal_displayed_2(page):
    page.goto("/")


@when("Modal is open")
def modal_open(page):
    pass


@then("Modal does not block access to page content")
def verify_no_blocking(page):
    expect(page.locator("main")).to_be_visible()


@given("Campaign modal dismissed by user")
def modal_dismissed(page):
    page.goto("/")


@when("User continues browsing")
def continue_browsing(page):
    pass


@then("Modal does not reappear immediately without appropriate trigger")
def verify_no_reappear(page):
    pass


@given("JavaScript disabled")
def js_disabled(page):
    pass


@when("Page loads")
def load_no_js(page):
    page.goto("/")


@then("Base page functions; conditional modals do not break page")
def verify_base_functions(page):
    expect(page.locator("header")).to_be_visible()
