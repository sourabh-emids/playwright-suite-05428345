"""Locators for emids_lp_010: Route hero CTA to FDCE experience."""
from playwright.sync_api import Locator, Page


class EmidsLp010HeroCtaLocators:
    """Locators for Hero CTA to FDCE routing verification."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def hero_cta(self) -> Locator:
        return self.page.locator('main a[href*="/forward-deployed-context-engineering/"]').first

    @property
    def hero_cta_all(self) -> Locator:
        return self.page.locator("main a").first
