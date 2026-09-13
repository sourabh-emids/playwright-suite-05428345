"""Locators for emids_lp_011: Optimize hero media loading."""
from playwright.sync_api import Locator, Page


class EmidsLp011HeroMediaLocators:
    """Locators for Hero media optimization verification."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def hero_media(self) -> Locator:
        return self.page.locator("main img, main video, main iframe").first

    @property
    def hero_video_poster(self) -> Locator:
        return self.page.locator("video[poster], video")

    @property
    def lazy_loaded_images(self) -> Locator:
        return self.page.locator('img[loading="lazy"]')
