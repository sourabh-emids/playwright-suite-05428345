"""Locators for Six featured solution items rendering (issue_0015)."""
from playwright.sync_api import Locator, Page


class FeaturedSolutionsLocators:
    """Locators for Featured Solutions section elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def solutions_section(self) -> Locator:
        return self.page.get_by_text("A portfolio of named solutions")

    @property
    def solution_cards(self) -> Locator:
        return self.page.locator(".solution-card, [data-solution], section a[href*='/solutions/']")

    @property
    def all_solutions_link(self) -> Locator:
        return self.page.get_by_role("link", name="All solutions").first

    @property
    def solution_titles(self) -> Locator:
        return self.page.locator("h3, h4, .solution-title")
