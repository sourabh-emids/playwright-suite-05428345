"""Locators for Capabilities mega-menu - EMIDS-LP-003"""
from playwright.sync_api import Page, Locator


class CapabilitiesMenuLocators:
    """Locators for Capabilities mega-menu elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def capabilities_nav(self) -> Locator:
        return self.page.get_by_role("navigation", name="Main Navigation").get_by_role("link", name="Capabilities")

    @property
    def capabilities_trigger(self) -> Locator:
        return self.page.get_by_role("button", name="Capabilities").first

    @property
    def ai_group(self) -> Locator:
        return self.page.get_by_text("AI").first

    @property
    def engineering_group(self) -> Locator:
        return self.page.get_by_text("Engineering").first

    @property
    def platforms_group(self) -> Locator:
        return self.page.get_by_text("Platforms").first

    @property
    def capability_links(self) -> Locator:
        return self.page.locator('a[href*="/capabilities/"]')
