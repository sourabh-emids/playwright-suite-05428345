"""Locators for the Capabilities section (issues 0020-0023)."""
from playwright.sync_api import Locator, Page


class CapabilitiesSectionLocators:
    """Locators for the Capabilities section."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def section(self) -> Locator:
        return self.page.locator("text=Capabilities").locator("..").locator("..")

    @property
    def ai_group(self) -> Locator:
        return self.page.get_by_text("AI")

    @property
    def engineering_group(self) -> Locator:
        return self.page.get_by_text("Engineering")

    @property
    def platforms_group(self) -> Locator:
        return self.page.get_by_text("Platforms")

    @property
    def capability_cards(self) -> Locator:
        return self.page.locator("text=/AI|Engineering|Platforms/").locator("..").locator("..").locator("article, div")
