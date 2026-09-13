"""Locators for emids_lp_008: Provide responsive accessible navigation."""
from playwright.sync_api import Locator, Page


class EmidsLp008ResponsiveNavLocators:
    """Locators for responsive accessible navigation verification."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def mobile_menu_button(self) -> Locator:
        return self.page.locator('[aria-label="Menu"], [aria-label="Open menu"], button:has-text("Menu")')

    @property
    def close_menu_button(self) -> Locator:
        return self.page.locator('[aria-label="Close menu"], button:has-text("Close")')

    @property
    def nav_buttons(self) -> Locator:
        return self.page.locator("nav button, header button")

    @property
    def interactive_elements(self) -> Locator:
        return self.page.locator("a[href], button, input, select, textarea, [tabindex='0']")
