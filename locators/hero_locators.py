"""Locators for the Hero module (issues 0009, 0010, 0011)."""
from playwright.sync_api import Locator, Page


class HeroLocators:
    """Locators for the Hero component."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def hero_section(self) -> Locator:
        return self.page.locator("main")

    @property
    def hero_h1(self) -> Locator:
        return self.page.get_by_role("heading", level=1)

    @property
    def hero_body_copy(self) -> Locator:
        return self.page.locator("main h2").first

    @property
    def hero_cta(self) -> Locator:
        return self.page.get_by_role("link", name="See How We Deliver Outcomes")

    @property
    def hero_media(self) -> Locator:
        return self.page.locator("main img, main video").first

    @property
    def hero_eyebrow(self) -> Locator:
        return self.page.locator("main h2, main h3").first

    @property
    def fdce_cta(self) -> Locator:
        return self.page.get_by_role("link", name="See How We Deliver Outcomes")
