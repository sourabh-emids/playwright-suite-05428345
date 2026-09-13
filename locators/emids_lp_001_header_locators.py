"""Locators for emids_lp_001: Render global header and Emids brand."""
from playwright.sync_api import Locator, Page


class HeaderLocators:
    """Header section locators."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def emids_logo(self) -> Locator:
        """Emids logo/brand link in header."""
        return self.page.get_by_role("link", name="Emids logo")

    @property
    def main_navigation(self) -> Locator:
        """Main navigation container."""
        return self.page.get_by_role("navigation", name="Main Navigation")

    @property
    def solutions_nav(self) -> Locator:
        """Solutions navigation item."""
        return self.page.get_by_role("link", name="Solutions")

    @property
    def capabilities_nav(self) -> Locator:
        """Capabilities navigation item."""
        return self.page.get_by_role("link", name="Capabilities")

    @property
    def industries_nav(self) -> Locator:
        """Industries navigation item."""
        return self.page.get_by_role("link", name="Industries")

    @property
    def insights_nav(self) -> Locator:
        """Insights navigation item."""
        return self.page.get_by_role("link", name="Insights")

    @property
    def company_nav(self) -> Locator:
        """Company navigation item."""
        return self.page.get_by_role("link", name="Company")

    @property
    def connect_cta(self) -> Locator:
        """Connect CTA in header."""
        return self.page.get_by_role("link", name="Connect").first

    @property
    def header_banner(self) -> Locator:
        """Header banner element."""
        return self.page.get_by_role("banner")
