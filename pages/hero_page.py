"""Page object for the Hero module (issues 0009, 0010, 0011)."""
from playwright.sync_api import Page, expect
from locators.hero_locators import HeroLocators


class HeroPage(HeroLocators):
    """Page object for Hero functionality."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

    def click_hero_cta(self) -> None:
        self.hero_cta.click()

    def get_h1_text(self) -> str:
        return self.hero_h1.text_content()

    def get_cta_href(self) -> str:
        return self.hero_cta.get_attribute("href")

    def is_media_visible(self) -> bool:
        return self.hero_media.is_visible() if self.hero_media.count() > 0 else False

    def get_current_url(self) -> str:
        return self.page.url
