"""Locators for issue_0037 - Google Tag Manager consent-governed loading."""
from playwright.sync_api import Locator


class Issue0037GTMConsentLocators:
    """Locators for GTM consent-governed loading."""

    @property
    def gtm_script(self) -> Locator:
        """Return the GTM script element."""
        return self.page.locator("script[src*='googletagmanager']")
