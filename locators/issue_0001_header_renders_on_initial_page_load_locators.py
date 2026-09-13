"""Locators for issue_0001: Render global header with navigation"""

from playwright.sync_api import Page, Locator


class Issue0001HeaderLocators:
    """Locators for the global header functionality."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def emids_logo(self) -> Locator:
        """Returns the Emids logo link in the header."""
        return self.page.get_by_role("link", name="Emids logo").first

    @property
    def navigation_list(self) -> Locator:
        """Returns the main navigation list."""
        return self.page.get_by_role("navigation", name="Main Navigation")

    @property
    def solutions_nav_button(self) -> Locator:
        """Returns the Solutions navigation button."""
        return self.page.get_by_role("button", name="Solutions")

    @property
    def capabilities_nav_button(self) -> Locator:
        """Returns the Capabilities navigation button."""
        return self.page.get_by_role("button", name="Capabilities")

    @property
    def industries_nav_button(self) -> Locator:
        """Returns the Industries navigation button."""
        return self.page.get_by_role("button", name="Industries")

    @property
    def insights_nav_button(self) -> Locator:
        """Returns the Insights navigation button."""
        return self.page.get_by_role("button", name="Insights")

    @property
    def company_nav_button(self) -> Locator:
        """Returns the Company navigation button."""
        return self.page.get_by_role("button", name="Company")

    @property
    def connect_cta_header(self) -> Locator:
        """Returns the Connect CTA in the header."""
        return self.page.get_by_role("link", name="Connect").first

    def get_all_nav_items(self) -> list[str]:
        """Returns list of navigation item names."""
        return ["Solutions", "Capabilities", "Industries", "Insights", "Company"]

    def get_connect_cta_count(self) -> Locator:
        """Returns locator for counting Connect CTA elements."""
        return self.page.get_by_role("link", name="Connect")
