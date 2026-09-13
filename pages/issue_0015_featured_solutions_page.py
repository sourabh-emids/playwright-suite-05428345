"""Page object for Six featured solution items rendering (issue_0015)."""
from playwright.sync_api import Page

from locators.issue_0015_featured_solutions_locators import FeaturedSolutionsLocators


class FeaturedSolutionsPage:
    """Page object for Featured Solutions section functionality."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = FeaturedSolutionsLocators(page)

    def goto_homepage(self) -> None:
        self.page.goto("/")

    def scroll_to_solutions(self) -> None:
        self.locators.solutions_section.scroll_into_view_if_needed()

    def get_solution_count(self) -> int:
        return self.locators.solution_cards.count()

    def get_solution_titles(self) -> list:
        return self.locators.solution_titles.all()
