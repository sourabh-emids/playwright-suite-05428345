"""Locators for emids_lp_014: Maintain semantic section hierarchy."""
from playwright.sync_api import Locator, Page


class EmidsLp014GlobalLocators:
    """Locators for semantic section hierarchy verification."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def h1_elements(self) -> Locator:
        return self.page.locator("h1")

    @property
    def h2_elements(self) -> Locator:
        return self.page.locator("h2")

    @property
    def main_landmark(self) -> Locator:
        return self.page.locator("main")

    @property
    def header_landmark(self) -> Locator:
        return self.page.locator("header")

    @property
    def footer_landmark(self) -> Locator:
        return self.page.locator("footer")

    @property
    def nav_landmark(self) -> Locator:
        return self.page.locator("nav")
