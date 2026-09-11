"""Locators for REQ-002: Main navigation menu items navigate to correct pages."""

from playwright.sync_api import Page, Locator


class Req002NavigationLocators:
    """Locators for navigation menu elements."""

    def __init__(self, page: Page):
        self._page = page

    @property
    def main_navigation(self) -> Locator:
        """Main navigation menu."""
        return self._page.get_by_role("navigation", name="Main Navigation")

    @property
    def solutions_nav_button(self) -> Locator:
        """Solutions navigation button."""
        return self.main_navigation.get_by_role("button", name="Solutions")

    @property
    def capabilities_nav_button(self) -> Locator:
        """Capabilities navigation button."""
        return self.main_navigation.get_by_role("button", name="Capabilities")

    @property
    def industries_nav_button(self) -> Locator:
        """Industries navigation button."""
        return self.main_navigation.get_by_role("button", name="Industries")

    @property
    def insights_nav_button(self) -> Locator:
        """Insights navigation button."""
        return self.main_navigation.get_by_role("button", name="Insights")

    @property
    def company_nav_button(self) -> Locator:
        """Company navigation button."""
        return self.main_navigation.get_by_role("button", name="Company")

    @property
    def connect_nav_link(self) -> Locator:
        """Connect link in navigation."""
        return self.main_navigation.get_by_role("link", name="Connect")

    @property
    def solutions_dropdown_items(self) -> Locator:
        """Items in Solutions dropdown."""
        return self._page.locator("nav >> text='Solutions'").locator("..").locator("a")

    @property
    def capabilities_dropdown_items(self) -> Locator:
        """Items in Capabilities dropdown."""
        return self._page.locator("nav >> text='Capabilities'").locator("..").locator("a")

    @property
    def industries_dropdown_items(self) -> Locator:
        """Items in Industries dropdown."""
        return self._page.locator("nav >> text='Industries'").locator("..").locator("a")

    @property
    def insights_dropdown_items(self) -> Locator:
        """Items in Insights dropdown."""
        return self._page.locator("nav >> text='Insights'").locator("..").locator("a")

    @property
    def company_dropdown_items(self) -> Locator:
        """Items in Company dropdown."""
        return self._page.locator("nav >> text='Company'").locator("..").locator("a")
