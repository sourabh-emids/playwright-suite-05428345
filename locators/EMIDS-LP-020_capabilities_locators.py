"""Locators for Capabilities section - EMIDS-LP-020, EMIDS-LP-021, EMIDS-LP-022, EMIDS-LP-023"""
from playwright.sync_api import Page, Locator


class CapabilitiesLocators:
    """Locators for Capabilities section elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def section(self) -> Locator:
        return self.page.get_by_text("Capabilities that deliver on ambitious goals")

    @property
    def ai_card(self) -> Locator:
        return self.page.get_by_text("AI").first

    @property
    def engineering_card(self) -> Locator:
        return self.page.get_by_text("Engineering").first

    @property
    def platforms_card(self) -> Locator:
        return self.page.get_by_text("Platforms").first

    @property
    def ai_capability_link(self) -> Locator:
        return self.page.get_by_role("link", name="AI").first

    @property
    def engineering_capability_link(self) -> Locator:
        return self.page.get_by_role("link", name="Digital Engineering").first
