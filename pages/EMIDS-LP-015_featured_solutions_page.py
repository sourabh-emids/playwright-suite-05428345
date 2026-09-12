"""Page object for Featured Solutions section - EMIDS-LP-015, EMIDS-LP-016, EMIDS-LP-017"""
from playwright.sync_api import Page, expect
from locators.EMIDS-LP-015_featured_solutions_locators import FeaturedSolutionsLocators


class FeaturedSolutionsPage:
    """Page object for Featured Solutions section functionality."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = FeaturedSolutionsLocators(page)

    def goto(self, path: str = "/") -> None:
        self.page.goto(path)

    def verify_section_visible(self) -> None:
        expect(self.locators.section).to_be_visible()

    def count_solutions(self) -> int:
        return self.locators.solution_cards.count()

    def verify_all_six_solutions(self) -> None:
        expect(self.locators.solution_01).to_be_visible()
        expect(self.locators.solution_02).to_be_visible()
        expect(self.locators.solution_03).to_be_visible()
        expect(self.locators.solution_04).to_be_visible()
        expect(self.locators.solution_05).to_be_visible()
        expect(self.locators.solution_06).to_be_visible()

    def click_all_solutions_cta(self) -> None:
        self.locators.all_solutions_cta.click()

    def get_all_solutions_url(self) -> str:
        return self.locators.all_solutions_cta.get_attribute("href")

    def verify_all_solutions_routes(self) -> bool:
        url = self.get_all_solutions_url()
        return url and "/solutions/" in url

    def tab_through_solutions(self) -> list[str]:
        focused = []
        for _ in range(self.locators.solution_cards.count() + 5):
            self.page.keyboard.press("Tab")
            focused.append(self.page.evaluate("document.activeElement.tagName"))
        return focused
