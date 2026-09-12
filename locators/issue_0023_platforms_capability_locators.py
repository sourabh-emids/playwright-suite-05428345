"""Locators for issue_0023 - Platforms capability taxonomy consistency."""
from playwright.sync_api import Locator


class Issue0023PlatformsCapabilityLocators:
    """Locators for Platforms capability."""

    @property
    def platforms_capability_section(self) -> Locator:
        """Return the Platforms capability section."""
        return self.page.locator("text=Platforms").first
