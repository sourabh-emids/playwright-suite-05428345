"""Locators for tc_002 - Main navigation menu items functionality."""
from playwright.sync_api import Locator, Page


class Tc002NavigationLocators:
    """Locators for navigation functionality."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def main_navigation(self) -> Locator:
        return self.page.locator('navigation[aria-label="Main Navigation"]')

    @property
    def solutions_link(self) -> Locator:
        return self.main_navigation.get_by_role("link", name="Solutions")

    @property
    def capabilities_link(self) -> Locator:
        return self.main_navigation.get_by_role("link", name="Capabilities")

    @property
    def industries_link(self) -> Locator:
        return self.main_navigation.get_by_role("link", name="Industries")

    @property
    def insights_link(self) -> Locator:
        return self.main_navigation.get_by_role("link", name="Insights")

    @property
    def company_link(self) -> Locator:
        return self.main_navigation.get_by_role("link", name="Company")

    @property
    def connect_link(self) -> Locator:
        return self.page.get_by_role("link", name="Connect").first

    @property
    def solutions_dropdown(self) -> Locator:
        return self.page.locator('[class*="Solutions"]').first

    @property
    def capabilities_dropdown(self) -> Locator:
        return self.page.locator('[class*="Capabilities"]').first

    @property
    def industries_dropdown(self) -> Locator:
        return self.page.locator('[class*="Industries"]').first

    @property
    def insights_dropdown(self) -> Locator:
        return self.page.locator('[class*="Insights"]').first

    @property
    def company_dropdown(self) -> Locator:
        return self.page.locator('[class*="Company"]').first

    @property
    def all_menu_items(self) -> Locator:
        return self.main_navigation.locator("li")

    def get_submenu_link(self, name: str) -> Locator:
        """Get a specific submenu link by name."""
        return self.page.get_by_role("link", name=name, exact=False)
