"""Page object for issue_0036 - Cookie Preferences control visibility in footer."""
from playwright.sync_api import Page, expect

from locators.issue_0036_cookie_preferences_locators import Issue0036CookiePreferencesLocators


class Issue0036CookiePreferencesPage:
    """Page object for cookie preferences."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0036CookiePreferencesLocators()
        self.locators.page = page

    def view_footer(self) -> None:
        """Scroll to the footer."""
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

    def cookie_settings_button_should_be_visible(self) -> None:
        """Verify cookie settings button is visible."""
        expect(self.locators.cookie_settings_button).to_be_visible()

    def click_cookie_settings(self) -> None:
        """Click the cookie settings button."""
        self.locators.cookie_settings_button.click()

    def cookie_preferences_should_open(self) -> None:
        """Verify cookie preferences modal opens."""
        # Cookie preferences widget should appear
        expect(self.page.locator("[class*='cookie'], [class*='consent']").first).to_be_visible()
