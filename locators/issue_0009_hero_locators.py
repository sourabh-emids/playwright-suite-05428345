"""Locators for issue_0009 - Hero section rendering and H1 uniqueness."""
from playwright.sync_api import Locator


class Issue0009HeroLocators:
    """Locators for hero section."""

    @property
    def hero_section(self) -> Locator:
        """Return the hero section."""
        return self.page.locator("main > div").first

    @property
    def h1_heading(self) -> Locator:
        """Return the H1 heading."""
        return self.page.get_by_role("heading", level=1).first

    @property
    def hero_subtitle(self) -> Locator:
        """Return the hero subtitle."""
        return self.page.get_by_role("heading", level=2).first
