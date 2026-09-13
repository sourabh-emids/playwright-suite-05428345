"""Locators for emids_lp_015-017: Featured Solutions."""
from playwright.sync_api import Locator, Page


class EmidsLp015FeaturedSolutionsLocators:
    """Locators for Featured Solutions section verification."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def solutions_section(self) -> Locator:
        return self.page.locator("section").filter(has=self.page.locator("text=Modernization as a Service, text=Interoperability, text=Cloud Migration").first).or_(
            self.page.locator("section").filter(has=self.page.locator("text=solutions").first)
        )

    @property
    def solution_cards(self) -> Locator:
        return self.page.locator('[class*="card"], [class*="solution"]')

    @property
    def all_solutions_cta(self) -> Locator:
        return self.page.locator('a:has-text("All solutions"), a:has-text("View all solutions")').first

    @property
    def solution_01(self) -> Locator:
        return self.page.locator("text=01").first

    @property
    def solution_06(self) -> Locator:
        return self.page.locator("text=06").first
