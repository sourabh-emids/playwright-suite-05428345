"""Locators for Wistia and YouTube embeds (issues 0043-0044)."""
from playwright.sync_api import Locator, Page


class MediaEmbedsLocators:
    """Locators for media embed elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def main_content(self) -> Locator:
        return self.page.locator("main")

    @property
    def wistia_embed(self) -> Locator:
        return self.page.locator("[data-wistia-id]")

    @property
    def youtube_embed(self) -> Locator:
        return self.page.locator("iframe[src*='youtube']")
