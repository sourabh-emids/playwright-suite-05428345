"""Locators for Capabilities overview rendering (issue_0020)."""
from playwright.sync_api import Locator, Page


class CapabilitiesOverviewLocators:
    """Locators for Capabilities overview elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def capabilities_section(self) -> Locator:
        return self.page.get_by_role("heading", name="Capabilities that deliver on ambitious goals")

    @property
    def ai_group(self) -> Locator:
        return self.page.get_by_text("AI", exact=False).first

    @property
    def engineering_group(self) -> Locator:
        return self.page.get_by_text("Engineering", exact=False).first

    @property
    def platforms_group(self) -> Locator:
        return self.page.get_by_text("Platforms", exact=False).first
