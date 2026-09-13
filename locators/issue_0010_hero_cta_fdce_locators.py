"""Locators for Hero CTA routes to FDCE experience (issue_0010)."""
from playwright.sync_api import Locator, Page


class HeroCTAFDCELocators:
    """Locators for Hero CTA FDCE elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def hero_cta(self) -> Locator:
        return self.page.get_by_role("link", name="See How We Deliver Outcomes").first
