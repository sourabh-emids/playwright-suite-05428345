"""Locators for issue_0011: Hero media loading optimization"""

from playwright.sync_api import Page, Locator


class Issue0011HeroMediaLocators:
    """Locators for Hero media loading optimization."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def hero_section(self) -> Locator:
        """Returns the hero section."""
        return self.page.locator("main > div:first-child").first

    @property
    def hero_h1(self) -> Locator:
        """Returns the hero H1 for text content verification."""
        return self.page.get_by_role("heading", level=1)

    @property
    def hero_media(self) -> Locator:
        """Returns hero media elements."""
        return self.page.locator("main img, main video").first
