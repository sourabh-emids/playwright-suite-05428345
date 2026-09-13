"""Locators for issue_0020: Capabilities overview render"""

from playwright.sync_api import Page, Locator


class Issue0020CapabilitiesLocators:
    """Locators for Capabilities overview."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def capabilities_section(self) -> Locator:
        """Returns the Capabilities section."""
        return self.page.get_by_text("Capabilities that deliver on ambitious goals").locator("..")

    @property
    def ai_group(self) -> Locator:
        """Returns the AI capability group."""
        return self.page.get_by_text("AI")

    @property
    def engineering_group(self) -> Locator:
        """Returns the Engineering capability group."""
        return self.page.get_by_text("Engineering")

    @property
    def platforms_group(self) -> Locator:
        """Returns the Platforms capability group."""
        return self.page.get_by_text("Platforms")
