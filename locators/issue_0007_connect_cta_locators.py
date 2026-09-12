"""Locators for issue_0007 - Header Connect CTA visibility and routing."""
from playwright.sync_api import Locator


class Issue0007ConnectCTALocators:
    """Locators for Header Connect CTA."""

    @property
    def header_connect_cta(self) -> Locator:
        """Return the Connect CTA in header."""
        return self.page.locator("header").get_by_role("link", name="Connect").first
