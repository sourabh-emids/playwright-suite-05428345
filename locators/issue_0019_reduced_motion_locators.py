"""Locators for issue_0019 - Reduced motion preference for partner animation."""
from playwright.sync_api import Locator


class Issue0019ReducedMotionLocators:
    """Locators for reduced motion behavior."""

    @property
    def partnerships_section(self) -> Locator:
        """Return the Partnerships section."""
        return self.page.locator("text=We've assembled the world's most powerful technology platforms")

    @property
    def partner_carousel(self) -> Locator:
        """Return the partner logo carousel/rail."""
        return self.page.locator("[class*='carousel'], [class*='rail'], [class*='logos']")
