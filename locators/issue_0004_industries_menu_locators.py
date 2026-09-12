"""Locators for issue_0004 - Industries mega-menu content."""
from playwright.sync_api import Locator


class Issue0004IndustriesMenuLocators:
    """Locators for Industries mega-menu."""

    @property
    def industries_nav_button(self) -> Locator:
        """Return the Industries navigation button."""
        return self.page.locator('button:has-text("Industries")')

    @property
    def consumer_link(self) -> Locator:
        """Return the Consumer industry link."""
        return self.page.get_by_role("link", name="Consumer")
