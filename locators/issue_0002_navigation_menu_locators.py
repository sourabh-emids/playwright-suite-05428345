"""Locators for issue_0002: Main navigation menu items work correctly."""
from playwright.sync_api import Page, Locator


class NavigationMenuLocators:
    """Locators for the main navigation menu."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def solutions_link(self) -> Locator:
        return self.page.locator("nav").get_by_role("link", name="Solutions")

    @property
    def capabilities_link(self) -> Locator:
        return self.page.locator("nav").get_by_role("link", name="Capabilities")

    @property
    def industries_link(self) -> Locator:
        return self.page.locator("nav").get_by_role("link", name="Industries")

    @property
    def insights_link(self) -> Locator:
        return self.page.locator("nav").get_by_role("link", name="Insights")

    @property
    def company_link(self) -> Locator:
        return self.page.locator("nav").get_by_role("link", name="Company")

    @property
    def connect_link(self) -> Locator:
        return self.page.locator("nav").get_by_role("link", name="Connect")
