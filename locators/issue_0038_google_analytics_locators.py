"""Locators for issue_0038 - Google Analytics post-consent measurement."""
from playwright.sync_api import Locator


class Issue0038GoogleAnalyticsLocators:
    """Locators for Google Analytics."""

    @property
    def ga_script(self) -> Locator:
        """Return the GA script element."""
        return self.page.locator("script[src*='google-analytics'], script[src*='gtag']")
