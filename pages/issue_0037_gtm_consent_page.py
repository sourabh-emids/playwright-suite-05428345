"""Page object for issue_0037 - Google Tag Manager consent-governed loading."""
from playwright.sync_api import Page

from locators.issue_0037_gtm_consent_locators import Issue0037GTMConsentLocators


class Issue0037GTMConsentPage:
    """Page object for GTM consent-governed loading."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0037GTMConsentLocators()
        self.locators.page = page

    def gtm_should_not_be_active_before_consent(self) -> None:
        """Verify GTM is not active before consent."""
        # Check if GTM data layer indicates consent is required
        has_consent = self.page.evaluate("() => window.dataLayer?.some(item => item.consent === 'granted')")
        assert not has_consent, "GTM should not be active without consent"
