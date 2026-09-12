"""Locators for issue_0022 - Engineering capability content rendering."""
from playwright.sync_api import Locator


class Issue0022EngineeringCapabilityLocators:
    """Locators for Engineering capability."""

    @property
    def engineering_capability_section(self) -> Locator:
        """Return the Engineering capability section."""
        return self.page.locator("text=Engineering").first
