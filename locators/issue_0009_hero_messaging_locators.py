"""Locators for Hero messaging and visual rendering (issue_0009)."""
from playwright.sync_api import Locator, Page


class HeroMessagingLocators:
    """Locators for Hero section elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def h1_heading(self) -> Locator:
        return self.page.get_by_role("heading", level=1)

    @property
    def hero_cta(self) -> Locator:
        return self.page.get_by_role("link", name="See How We Deliver Outcomes").first

    @property
    def hero_section(self) -> Locator:
        return self.page.locator("main > div").first

    @property
    def eyebrow_text(self) -> Locator:
        return self.page.locator("main").get_by_text("AI · Engineering · Platforms").first

    @property
    def body_copy(self) -> Locator:
        return self.page.locator("main h2").first

    @property
    def h1_elements(self) -> Locator:
        return self.page.locator("h1")

    @property
    def hero_media(self) -> Locator:
        return self.page.locator("main img, main video").first
