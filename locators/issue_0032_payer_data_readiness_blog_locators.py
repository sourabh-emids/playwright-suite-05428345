"""Locators for issue_0032 - Payer data readiness blog card display."""
from playwright.sync_api import Locator


class Issue0032PayerDataReadinessBlogLocators:
    """Locators for Payer data readiness blog card."""

    @property
    def payer_data_card(self) -> Locator:
        """Return the Payer data readiness blog card."""
        return self.page.get_by_role("link", name="Payers: Is Your Data Ready for AI?")
