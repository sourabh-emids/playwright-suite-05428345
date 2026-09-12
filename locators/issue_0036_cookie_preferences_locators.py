"""Locators for issue_0036 - Cookie Preferences control visibility in footer."""
from playwright.sync_api import Locator


class Issue0036CookiePreferencesLocators:
    """Locators for cookie preferences."""

    @property
    def cookie_settings_button(self) -> Locator:
        """Return the cookie settings button."""
        return self.page.get_by_role("button", name="Open cookie settings widget")
