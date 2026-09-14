"""Page object for the Featured Solutions module (issues 0015, 0016, 0017)."""
from playwright.sync_api import Page, expect
from locators.featured_solutions_locators import FeaturedSolutionsLocators


class FeaturedSolutionsPage(FeaturedSolutionsLocators):
    """Page object for Featured Solutions functionality."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

    def click_all_solutions_cta(self) -> None:
        self.all_solutions_cta.click()

    def get_solution_count(self) -> int:
        return self.solution_cards.count()

    def get_numbering_order(self) -> list:
        numbers = self.solution_numbers.all()
        return [n.text_content() for n in numbers]
