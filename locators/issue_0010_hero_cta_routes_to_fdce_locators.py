"""Locators for issue_0010: Hero CTA routes to FDCE"""

from playwright.sync_api import Page, Locator


class Issue0010HeroCTALocators:
    """Locators for the Hero CTA."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def hero_cta(self) -> Locator:
        """Returns the hero CTA link."""
        return self.page.get_by_role("link", name="See How We Deliver Outcomes")
