"""Locators for the Capabilities Mega-Menu (issue_0003)."""
from playwright.sync_api import Locator, Page


class CapabilitiesMenuLocators:
    """Locators for the Capabilities mega-menu component."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def capabilities_trigger(self) -> Locator:
        return self.page.get_by_role("button", name="Capabilities")

    @property
    def capabilities_menu(self) -> Locator:
        return self.page.locator('[aria-label*="Capabilities"], .capabilities-menu')

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
        return self.page.locator('.capabilities-menu a, [aria-label*="Capabilities"] a')

    @property
    def digital_engineering_link(self) -> Locator:
        return self.page.get_by_role("link", name="Digital Engineering")

    @property
    def low_code_link(self) -> Locator:
        return self.page.get_by_role("link", name="Low-Code Solutions")
