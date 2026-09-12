"""Locators for issue_0001 - Header visibility and global navigation."""
from playwright.sync_api import Locator


class Issue0001HeaderLocators:
    """Locators for header visibility and global navigation."""

    @property
    def header_banner(self) -> Locator:
        """Return the header banner region."""
        return self.page.locator("banner")

    @property
    def main_navigation(self) -> Locator:
        """Return the main navigation element."""
        return self.page.get_by_role("navigation", name="Main Navigation")

    @property
    def logo_link(self) -> Locator:
        """Return the logo link."""
        return self.page.get_by_role("link", name="Emids logo")

    @property
    def solutions_link(self) -> Locator:
        """Return the Solutions navigation link."""
        return self.main_navigation.get_by_role("link", name="Solutions")

    @property
    def capabilities_link(self) -> Locator:
        """Return the Capabilities navigation link."""
        return self.main_navigation.get_by_role("link", name="Capabilities")

    @property
    def industries_link(self) -> Locator:
        """Return the Industries navigation link."""
        return self.main_navigation.get_by_role("link", name="Industries")

    @property
    def insights_link(self) -> Locator:
        """Return the Insights navigation link."""
        return self.main_navigation.get_by_role("link", name="Insights")

    @property
    def company_link(self) -> Locator:
        """Return the Company navigation link."""
        return self.main_navigation.get_by_role("link", name="Company")

    @property
    def header_connect_cta(self) -> Locator:
        """Return the Connect CTA in header."""
        return self.page.locator("header").get_by_role("link", name="Connect")
