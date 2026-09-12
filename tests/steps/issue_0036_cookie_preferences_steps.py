"""Step definitions for issue_0036 - Cookie Preferences control visibility in footer."""
from pytest_bdd import given, then, when

from pages.issue_0036_cookie_preferences_page import Issue0036CookiePreferencesPage


@given("I navigate to the homepage")
def navigate_to_homepage(page: Issue0036CookiePreferencesPage):
    """Navigate to the homepage."""
    page.page.goto("/")


@when("I view the footer")
def view_footer(page: Issue0036CookiePreferencesPage):
    """View the footer."""
    page.view_footer()


@then("the cookie settings button should be visible")
def cookie_settings_visible(page: Issue0036CookiePreferencesPage):
    """Verify cookie settings button is visible."""
    page.cookie_settings_button_should_be_visible()


@when("clicking it should open cookie preferences")
def click_cookie_settings(page: Issue0036CookiePreferencesPage):
    """Click cookie settings button."""
    page.click_cookie_settings()


@then("clicking it should open cookie preferences")
def cookie_preferences_open(page: Issue0036CookiePreferencesPage):
    """Verify cookie preferences opens."""
    page.cookie_preferences_should_open()
