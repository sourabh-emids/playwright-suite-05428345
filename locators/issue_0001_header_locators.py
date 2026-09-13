"""Locators for Global header visibility and Emids brand link (issue_0001)."""
from playwright.sync_api import Locator, Page


class HeaderLocators:
    """Locators for header navigation elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def header(self) -> Locator:
        return self.page.locator("header")

    @property
    def logo(self) -> Locator:
        return self.page.get_by_role("link", name="Emids logo").or_(self.page.locator("a[href='/']").first)

    @property
    def solutions_button(self) -> Locator:
        return self.page.get_by_role("button", name="Solutions")

    @property
    def capabilities_button(self) -> Locator:
        return self.page.get_by_role("button", name="Capabilities")

    @property
    def industries_button(self) -> Locator:
        return self.page.get_by_role("button", name="Industries")

    @property
    def insights_button(self) -> Locator:
        return self.page.get_by_role("button", name="Insights")

    @property
    def company_button(self) -> Locator:
        return self.page.get_by_role("button", name="Company")

    @property
    def connect_cta(self) -> Locator:
        return self.page.get_by_role("link", name="Connect").first

    @property
    def navigation(self) -> Locator:
        return self.page.get_by_role("navigation", name="Main Navigation")

    @property
    def nav_items(self) -> Locator:
        return self.page.locator("header nav button, header nav a")

    @property
    def all_nav_buttons(self) -> Locator:
        return self.page.locator("header button")
