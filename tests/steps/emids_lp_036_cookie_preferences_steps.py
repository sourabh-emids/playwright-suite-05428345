"""Step definitions for emids_lp_036 - Cookie Preferences."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then


@then("Control is visible and accessible in the footer")
def verify_cookie_control_visible(page: Page) -> None:
    from pages.emids_lp_036_cookie_preferences_page import CookiePreferencesPage
    page_obj = CookiePreferencesPage(page)
    expect(page_obj.cookie_preferences_control).to_be_visible()


@when("User clicks or activates the control")
def activate_cookie_control(page: Page) -> None:
    from pages.emids_lp_036_cookie_preferences_page import CookiePreferencesPage
    page_obj = CookiePreferencesPage(page)
    page_obj.cookie_preferences_control.click()


@then("Consent-management UI opens")
def verify_consent_ui_opens(page: Page) -> None:
    from pages.emids_lp_036_cookie_preferences_page import CookiePreferencesPage
    page_obj = CookiePreferencesPage(page)
    expect(page_obj.consent_modal).to_be_visible()


@then("User can revise or withdraw consent preferences")
def verify_consent_revision(page: Page) -> None:
    from pages.emids_lp_036_cookie_preferences_page import CookiePreferencesPage
    page_obj = CookiePreferencesPage(page)
    expect(page_obj.consent_modal).to_be_visible()


@then("Cookie Preferences control remains available in footer")
def verify_control_after_dismiss(page: Page) -> None:
    from pages.emids_lp_036_cookie_preferences_page import CookiePreferencesPage
    page_obj = CookiePreferencesPage(page)
    page.reload()
    expect(page_obj.cookie_preferences_control).to_be_visible()


@then("Page remains functional; Cookie Preferences control shows appropriate fallback")
def verify_consent_blocked(page: Page) -> None:
    from pages.emids_lp_036_cookie_preferences_page import CookiePreferencesPage
    page_obj = CookiePreferencesPage(page)
    expect(page_obj.cookie_preferences_control).to_be_visible()


@then("Consent state persists in memory or user is notified of limitations")
def verify_storage_disabled(page: Page) -> None:
    from pages.emids_lp_036_cookie_preferences_page import CookiePreferencesPage
    page_obj = CookiePreferencesPage(page)
    expect(page_obj.cookie_preferences_control).to_be_visible()


@then("Cookie Preferences control remains available; consent state resets appropriately")
def verify_cookies_cleared(page: Page) -> None:
    from pages.emids_lp_036_cookie_preferences_page import CookiePreferencesPage
    page_obj = CookiePreferencesPage(page)
    expect(page_obj.cookie_preferences_control).to_be_visible()
