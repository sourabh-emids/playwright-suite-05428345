"""Locators for issue_0010 - Hero CTA routing to FDCE experience."""
from playwright.sync_api import Locator


class Issue0010HeroCTALocators:
    """Locators for hero CTA."""

    @property
    def hero_cta(self) -> Locator:
        """Return the hero CTA link."""
        return self.page.get_by_role("link", name="See How We Deliver Outcomes")
