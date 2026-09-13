"""Locators for emids_lp_050-054: Accessibility and SEO."""
from playwright.sync_api import Locator, Page


class EmidsLp050AccessibilityLocators:
    """Locators for accessibility verification."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def all_interactive_elements(self) -> Locator:
        return self.page.locator("a, button, input, select, textarea, [tabindex='0']")

    @property
    def images(self) -> Locator:
        return self.page.locator("img")

    @property
    def forms(self) -> Locator:
        return self.page.locator("form")

    @property
    def page_title(self) -> Locator:
        return self.page.locator("title")

    @property
    def meta_description(self) -> Locator:
        return self.page.locator('meta[name="description"]')

    @property
    def canonical_url(self) -> Locator:
        return self.page.locator('link[rel="canonical"]')

    @property
    def og_tags(self) -> Locator:
        return self.page.locator('meta[property^="og:"]')
