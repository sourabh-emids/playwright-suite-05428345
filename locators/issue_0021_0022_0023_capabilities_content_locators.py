"""Locators for AI, Engineering, and Platforms capability content rendering (issues 0021-0023)."""
from playwright.sync_api import Locator, Page


class CapabilitiesContentLocators:
    """Locators for Capabilities content elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def capabilities_section(self) -> Locator:
        return self.page.get_by_role("heading", name="Capabilities that deliver on ambitious goals")

    @property
    def ai_panel(self) -> Locator:
        return self.page.get_by_text("AI", exact=False).first

    @property
    def engineering_panel(self) -> Locator:
        return self.page.get_by_text("Engineering", exact=False).first

    @property
    def platforms_panel(self) -> Locator:
        return self.page.get_by_text("Platforms", exact=False).first
