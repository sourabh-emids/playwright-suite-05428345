"""Locators for Hero media loading optimization (issue_0011)."""
from playwright.sync_api import Locator, Page


class HeroMediaOptimizationLocators:
    """Locators for Hero media optimization elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def hero_section(self) -> Locator:
        return self.page.locator("main > div").first

    @property
    def hero_text(self) -> Locator:
        return self.page.locator("main h1, main h2").first

    @property
    def hero_images(self) -> Locator:
        return self.page.locator("main img")
