"""Locators for Header section - EMIDS-LP-001"""
from playwright.sync_api import Page, Locator


class HeaderLocators:
    """Locators for header elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def emids_logo(self) -> Locator:
        return self.page.get_by_role("link", name="Emids logo")

    @property
    def main_navigation(self) -> Locator:
        return self.page.get_by_role("navigation", name="Main Navigation")

    @property
    def solutions_nav(self) -> Locator:
        return self.main_navigation.get_by_role("link", name="Solutions")

    @property
    def capabilities_nav(self) -> Locator:
        return self.main_navigation.get_by_role("link", name="Capabilities")

    @property
    def industries_nav(self) -> Locator:
        return self.main_navigation.get_by_role("link", name="Industries")

    @property
    def insights_nav(self) -> Locator:
        return self.main_navigation.get_by_role("link", name="Insights")

    @property
    def company_nav(self) -> Locator:
        return self.main_navigation.get_by_role("link", name="Company")

    @property
    def header_connect_cta(self) -> Locator:
        return self.page.locator("header").get_by_role("link", name="Connect").first

    @property
    def all_nav_items(self) -> Locator:
        return self.main_navigation.locator("li a")

    @property
    def header_element(self) -> Locator:
        return self.page.locator("header").first
