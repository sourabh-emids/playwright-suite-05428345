"""Locators for emids_lp_009: Render hero messaging and visual."""
from playwright.sync_api import Locator, Page


class EmidsLp009HeroLocators:
    """Locators for Hero section verification."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def hero_section(self) -> Locator:
        return self.page.locator("section, [class*='hero'], main > div").first

    @property
    def h1_heading(self) -> Locator:
        return self.page.locator("h1").first

    @property
    def hero_title(self) -> Locator:
        return self.page.locator("h1").first

    @property
    def hero_cta(self) -> Locator:
        return self.page.locator("section a, main a").first

    @property
    def hero_eyebrow(self) -> Locator:
        return self.page.locator('[class*="eyebrow"], [class*="tagline"]').first

    @property
    def hero_media(self) -> Locator:
        return self.page.locator("img, video, iframe").first

    @property
    def hero_supporting_content(self) -> Locator:
        return self.page.locator("h2, p").first
