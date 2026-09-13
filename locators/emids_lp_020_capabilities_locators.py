"""Locators for emids_lp_020-023: Capabilities section."""
from playwright.sync_api import Locator, Page


class EmidsLp020CapabilitiesLocators:
    """Locators for Capabilities section verification."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def capabilities_section(self) -> Locator:
        return self.page.locator("section").filter(has=self.page.locator("text=Capabilities"))

    @property
    def ai_capability_group(self) -> Locator:
        return self.capabilities_section.locator("text=AI").first

    @property
    def engineering_capability_group(self) -> Locator:
        return self.capabilities_section.locator("text=Engineering").first

    @property
    def platforms_capability_group(self) -> Locator:
        return self.capabilities_section.locator("text=Platforms").first

    @property
    def capability_cards(self) -> Locator:
        return self.capabilities_section.locator('[class*="card"], [class*="capability"]')
