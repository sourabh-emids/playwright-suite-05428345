"""Locators for the Global Header Navigation (issue_0001)."""
from playwright.sync_api import Locator, Page


class HeaderLocators:
    """Locators for the header component."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def header(self) -> Locator:
        return self.page.locator("header")

    @property
    def logo(self) -> Locator:
        return self.page.get_by_role("link", name="Emids logo")

    @property
    def navigation(self) -> Locator:
        return self.page.get_by_role("navigation", name="Main Navigation")

    @property
    def nav_items(self) -> Locator:
        return self.page.locator("nav[role='navigation'] a, header a")

    @property
    def solutions_nav(self) -> Locator:
        return self.page.get_by_role("button", name="Solutions")

    @property
    def capabilities_nav(self) -> Locator:
        return self.page.get_by_role("button", name="Capabilities")

    @property
    def industries_nav(self) -> Locator:
        return self.page.get_by_role("button", name="Industries")

    @property
    def insights_nav(self) -> Locator:
        return self.page.get_by_role("button", name="Insights")

    @property
    def company_nav(self) -> Locator:
        return self.page.get_by_role("button", name="Company")

    @property
    def connect_cta(self) -> Locator:
        return self.page.get_by_role("link", name="Connect").first

    @property
    def solutions_menu(self) -> Locator:
        return self.page.locator('[aria-label="Solutions menu"], .solutions-menu, nav button:has-text("Solutions") + *')

    @property
    def mobile_menu_trigger(self) -> Locator:
        return self.page.get_by_role("button", name="Menu")
