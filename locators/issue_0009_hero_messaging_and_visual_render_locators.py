"""Locators for issue_0009: Hero messaging and visual render"""

from playwright.sync_api import Page, Locator


class Issue0009HeroLocators:
    """Locators for the Hero section."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def hero_section(self) -> Locator:
        """Returns the hero section."""
        return self.page.locator("main > div:first-child").first

    @property
    def h1_heading(self) -> Locator:
        """Returns the H1 heading."""
        return self.page.get_by_role("heading", level=1)

    @property
    def hero_cta(self) -> Locator:
        """Returns the hero CTA button."""
        return self.page.get_by_role("link", name="See How We Deliver Outcomes")

    @property
    def eyebrow_text(self) -> Locator:
        """Returns the eyebrow text."""
        return self.page.get_by_text("AI · Engineering · Platforms")

    @property
    def hero_image(self) -> Locator:
        """Returns the hero image if present."""
        return self.page.locator("main img").first


class Issue0009HeroLocators:
    """Locators for Hero messaging and visual render."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def h1(self) -> Locator:
        """Returns the H1 heading."""
        return self.page.get_by_role("heading", level=1)

    @property
    def hero_cta(self) -> Locator:
        """Returns the hero CTA."""
        return self.page.get_by_text("See How We Deliver Outcomes")

    @property
    def hero_media(self) -> Locator:
        """Returns hero media elements."""
        return self.page.locator("picture img, video").first
