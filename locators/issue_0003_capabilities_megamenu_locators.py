"""Locators for Capabilities mega-menu implementation (issue_0003)."""
from playwright.sync_api import Locator, Page


class CapabilitiesMegamenuLocators:
    """Locators for Capabilities mega-menu elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def capabilities_button(self) -> Locator:
        return self.page.get_by_role("button", name="Capabilities")

    @property
    def ai_group(self) -> Locator:
        return self.page.get_by_text("AI", exact=False).first

    @property
    def engineering_group(self) -> Locator:
        return self.page.get_by_text("Engineering", exact=False).first

    @property
    def platforms_group(self) -> Locator:
        return self.page.get_by_text("Platforms", exact=False).first

    @property
    def capability_links(self) -> Locator:
        return self.page.locator(".capabilities-menu a, [aria-label*='capabilities'] a")

    @property
    def menu_visible(self) -> Locator:
        return self.page.get_by_text("AI").first
