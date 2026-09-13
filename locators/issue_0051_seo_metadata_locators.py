"""Locators for SEO metadata and crawlable structure (issue_0051)."""
from playwright.sync_api import Locator, Page


class SEOMetadataLocators:
    """Locators for SEO metadata elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def page_title(self) -> Locator:
        return self.page.locator("title")

    @property
    def meta_description(self) -> Locator:
        return self.page.locator("meta[name='description']")

    @property
    def canonical_url(self) -> Locator:
        return self.page.locator("link[rel='canonical']")

    @property
    def og_metadata(self) -> Locator:
        return self.page.locator("meta[property^='og:']")

    @property
    def h1_heading(self) -> Locator:
        return self.page.locator("h1").first
