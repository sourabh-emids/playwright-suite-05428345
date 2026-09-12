"""Locators for issue_0011 - Hero media optimization and load behavior."""
from playwright.sync_api import Locator


class Issue0011HeroMediaLocators:
    """Locators for hero media."""

    @property
    def hero_section(self) -> Locator:
        """Return the hero section."""
        return self.page.locator("main > div").first

    @property
    def hero_images(self) -> Locator:
        """Return images in the hero section."""
        return self.hero_section.locator("img")
