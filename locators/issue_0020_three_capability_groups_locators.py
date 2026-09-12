"""Locators for issue_0020 - Three capability groups visibility and content."""
from playwright.sync_api import Locator


class Issue0020ThreeCapabilityGroupsLocators:
    """Locators for three capability groups."""

    @property
    def capabilities_section(self) -> Locator:
        """Return the Capabilities section."""
        return self.page.locator("text=Capabilities that deliver on ambitious goals")

    @property
    def ai_capability(self) -> Locator:
        """Return the AI capability element."""
        return self.page.locator("text=AI").first

    @property
    def engineering_capability(self) -> Locator:
        """Return the Engineering capability element."""
        return self.page.locator("text=Engineering").first

    @property
    def platforms_capability(self) -> Locator:
        """Return the Platforms capability element."""
        return self.page.locator("text=Platforms").first
