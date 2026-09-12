"""Locators for issue_0008 - Responsive navigation behavior."""
from playwright.sync_api import Locator


class Issue0008ResponsiveNavLocators:
    """Locators for responsive navigation."""

    @property
    def main_navigation(self) -> Locator:
        """Return the main navigation element."""
        return self.page.get_by_role("navigation", name="Main Navigation")

    @property
    def connect_cta(self) -> Locator:
        """Return the Connect CTA."""
        return self.page.locator("header").get_by_role("link", name="Connect").first

    @property
    def mobile_menu_toggle(self) -> Locator:
        """Return the mobile menu toggle button."""
        return self.page.locator("[class*='mobile'] button, [aria-label*='menu'], button[aria-expanded]")
