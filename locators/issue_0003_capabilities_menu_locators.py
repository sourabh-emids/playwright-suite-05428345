"""Locators for issue_0003 - Capabilities mega-menu accessibility."""
from playwright.sync_api import Locator


class Issue0003CapabilitiesMenuLocators:
    """Locators for Capabilities mega-menu."""

    @property
    def capabilities_nav_button(self) -> Locator:
        """Return the Capabilities navigation button."""
        return self.page.locator('button:has-text("Capabilities")')

    @property
    def ai_header(self) -> Locator:
        """Return the 'AI' header in capabilities menu."""
        return self.page.locator("text=AI").first

    @property
    def engineering_header(self) -> Locator:
        """Return the 'Engineering' header in capabilities menu."""
        return self.page.locator("text=Engineering").first

    @property
    def platforms_header(self) -> Locator:
        """Return the 'Platforms' header in capabilities menu."""
        return self.page.locator("text=Platforms").first
