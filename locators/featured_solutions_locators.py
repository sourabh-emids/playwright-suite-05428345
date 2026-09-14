"""Locators for the Featured Solutions module (issues 0015, 0016, 0017)."""
from playwright.sync_api import Locator, Page


class FeaturedSolutionsLocators:
    """Locators for the Featured Solutions section."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def section(self) -> Locator:
        return self.page.locator("text=Featured solutions").locator("..").locator("..")

    @property
    def solution_cards(self) -> Locator:
        return self.page.locator('a[href*="/solutions/"]')

    @property
    def all_solutions_cta(self) -> Locator:
        return self.page.get_by_role("link", name="All solutions")

    @property
    def solution_numbers(self) -> Locator:
        return self.page.locator("text=/^0[1-6]$/")
