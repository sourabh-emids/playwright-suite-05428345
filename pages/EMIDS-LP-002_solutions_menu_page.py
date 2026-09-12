"""Page object for Solutions mega-menu - EMIDS-LP-002"""
from playwright.sync_api import Page, expect
from locators.EMIDS-LP-002_solutions_menu_locators import SolutionsMenuLocators


class SolutionsMenuPage:
    """Page object for Solutions mega-menu functionality."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = SolutionsMenuLocators(page)

    def goto(self, path: str = "/") -> None:
        self.page.goto(path)

    def open_solutions_menu(self) -> None:
        self.locators.solutions_trigger.click()

    def hover_solutions_menu(self) -> None:
        self.locators.solutions_nav.hover()

    def close_menu_with_escape(self) -> None:
        self.page.keyboard.press("Escape")

    def get_solution_links(self) -> list[str]:
        links = []
        for i in range(self.locators.solution_links.count()):
            link = self.locators.solution_links.nth(i)
            href = link.get_attribute("href")
            if href:
                links.append(href)
        return links

    def verify_menu_open(self) -> None:
        expect(self.locators.solutions_by_initiative).to_be_visible()

    def click_solution_link(self, index: int = 0) -> None:
        self.locators.solution_links.nth(index).click()
