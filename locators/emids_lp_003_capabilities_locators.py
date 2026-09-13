"""Locators for emids_lp_003: Implement Capabilities mega-menu."""
from playwright.sync_api import Locator, Page


class EmidsLp003CapabilitiesLocators:
    """Locators for Capabilities mega-menu verification."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def capabilities_button(self) -> Locator:
        return self.page.get_by_role("button", name="Capabilities")

    @property
    def capabilities_menu(self) -> Locator:
        return self.page.locator('[role="menu"], .mega-menu').filter(has=self.page.get_by_role("button", name="Capabilities"))

    @property
    def ai_group(self) -> Locator:
        return self.page.locator("text=AI").first

    @property
    def engineering_group(self) -> Locator:
        return self.page.locator("text=Engineering").first

    @property
    def platforms_group(self) -> Locator:
        return self.page.locator("text=Platforms").first

    @property
    def capability_links(self) -> Locator:
        return self.capabilities_menu.locator("a")
