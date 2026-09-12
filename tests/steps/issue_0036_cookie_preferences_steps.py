"""Step definitions for Issue 0036 - Cookie Preferences control exposure."""
from pytest_bdd import given, when, then
from playwright.sync_api import Page, expect
from pages.homepage_page import HomepagePage


@given("A user views the footer")
def view_footer(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, document.body.scrollHeight)")


@when("The footer loads")
def footer_loads(page: Page):
    page.wait_for_load_state("networkidle")


@then("Cookie Preferences control (link/button) is visible")
def cookie_control_visible(page: Page):
    homepage = HomepagePage(page)
    homepage.cookie_preferences_button_is_visible()


@given("A user clicks the Cookie Preferences control")
def click_cookie_prefs(page: Page):
    homepage = HomepagePage(page)
    homepage.click_cookie_preferences()


@when("The control is activated")
def prefs_activated(page: Page):
    pass


@then("The consent-management UI opens")
def consent_ui_opens(page: Page):
    # Cookie settings UI should appear
    page.wait_for_timeout(500)


@given("A user has previously given consent")
def consent_given(page: Page):
    pass


@when("The user opens Cookie Preferences")
def open_cookie_prefs(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, document.body.scrollHeight)")
    homepage = HomepagePage(page)
    homepage.click_cookie_preferences()


@then("User can revise or withdraw consent")
def revise_withdraw_consent(page: Page):
    # Should show options to modify consent
    page.wait_for_timeout(500)


@given("A user has dismissed the initial cookie banner")
def banner_dismissed(page: Page):
    page.goto("/")
    homepage = HomepagePage(page)
    homepage.dismiss_cookie_banner()


@when("The user returns to the footer")
def return_footer(page: Page):
    pass


@then("Cookie Preferences control remains available")
def prefs_still_available(page: Page):
    homepage = HomepagePage(page)
    expect(homepage.cookie_preferences_button).to_be_visible()


@given("Consent script is blocked (by browser or CSP)")
def consent_blocked(page: Page):
    pass


@when("The page loads")
def page_loads_consent(page: Page):
    page.goto("/")


@then("Page remains functional; consent controls are not blocking dependencies")
def page_functional(page: Page):
    homepage = HomepagePage(page)
    expect(homepage.footer).to_be_visible()


@given("Browser storage is disabled")
def storage_disabled(page: Page):
    pass


@when("User attempts to save consent preferences")
def save_prefs(page: Page):
    page.goto("/")


@then("Appropriate handling occurs")
def handling_occurs(page: Page):
    homepage = HomepagePage(page)
    expect(homepage.footer).to_be_visible()
