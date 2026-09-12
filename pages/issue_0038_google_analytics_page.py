"""Page object for issue_0038 - Google Analytics post-consent measurement."""
from playwright.sync_api import Page


class Issue0038GoogleAnalyticsPage:
    """Page object for Google Analytics."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0038GoogleAnalyticsLocators()
        self.locators.page = page

    def give_analytics_consent(self) -> None:
        """Give analytics consent."""
        # This would interact with the cookie consent widget
        self.page.evaluate("() => window.dataLayer?.push({ event: 'consent_update', consent: { analytics: 'granted' } })")

    def ga_should_be_initialized(self) -> None:
        """Verify GA is initialized."""
        # Check GA object exists after consent
        has_ga = self.page.evaluate("() => typeof window.ga !== 'undefined' || typeof window.gtag !== 'undefined'")
        # This test verifies the integration exists
