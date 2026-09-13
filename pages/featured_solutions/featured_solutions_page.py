"""Page object for emids_lp_015: Render six featured solution items."""
from playwright.sync_api import Page, expect
from locators.emids_lp_014_global_locators import FeaturedSolutionsLocators


class FeaturedSolutionsPage:
    """Featured Solutions section page object."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = FeaturedSolutionsLocators(page)

    def navigate(self) -> None:
        """Navigate to homepage."""
        self.page.goto("/")

    def scroll_to_section(self) -> None:
        """Scroll to Featured Solutions section."""
        self.locators.section_heading.scroll_into_view_if_needed()

    def get_solution_count(self) -> int:
        """Get count of solution cards."""
        return self.locators.all_solutions.count()

    def get_solution_numbers(self) -> list[str]:
        """Get solution number labels."""
        numbers = []
        for i in range(1, 7):
            num = self.page.locator(f"text={i:02d}")
            if num.count() > 0:
                numbers.append(f"{i:02d}")
        return numbers

    def get_solution_titles(self) -> list[str]:
        """Get solution titles."""
        titles = []
        for loc in [self.locators.solution_01, self.locators.solution_02,
                    self.locators.solution_03, self.locators.solution_04,
                    self.locators.solution_05, self.locators.solution_06]:
            try:
                name = loc.get_attribute("name") or ""
                titles.append(name)
            except Exception:
                pass
        return titles

    def click_solution(self, number: int) -> None:
        """Click a solution by number."""
        solutions = {
            1: self.locators.solution_01,
            2: self.locators.solution_02,
            3: self.locators.solution_03,
            4: self.locators.solution_04,
            5: self.locators.solution_05,
            6: self.locators.solution_06,
        }
        solutions[number].click()

    def click_all_solutions_cta(self) -> None:
        """Click All Solutions CTA."""
        self.locators.all_solutions_cta.click()
