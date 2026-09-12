"""Locators for Hero section - EMIDS-LP-009, EMIDS-LP-010, EMIDS-LP-011"""
from playwright.sync_api import Page, Locator


class HeroLocators:
    """Locators for Hero section elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def h1_heading(self) -> Locator:
        return self.page.locator("h1").first

    @property
    def hero_cta(self) -> Locator:
        return self.page.get_by_role("link", name="See How We Deliver Outcomes")

    @property
    def hero_section(self) -> Locator:
        return self.page.locator("main > div").first

    @property
    def hero_media(self) -> Locator:
        return self.hero_section.locator("img, video")

    @property
    def hero_copy(self) -> Locator:
        return self.page.locator("h2").first
