"""Page object for Solutions mega-menu implementation (issue_0002)."""
from playwright.sync_api import Page, expect

from locators.issue_0002_solutions_megamenu_locators import SolutionsMegamenuLocators


class SolutionsMegamenuPage:
    """Page object for Solutions mega-menu functionality."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = SolutionsMegamenuLocators(page)

    def goto_homepage(self) -> None:
        self.page.goto("/")

    def hover_solutions(self) -> None:
        self.locators.solutions_button.hover()
        self.page.wait_for_timeout(300)

    def click_solutions(self) -> None:
        self.locators.solutions_button.click()

    def tab_to_solutions(self) -> None:
        self.locators.solutions_button.focus()
        self.page.keyboard.press("Tab")

    def press_enter_on_solutions(self) -> None:
        self.locators.solutions_button.focus()
        self.page.keyboard.press("Enter")

    def press_space_on_solutions(self) -> None:
        self.locators.solutions_button.focus()
        self.page.keyboard.press(" ")

    def press_escape(self) -> None:
        self.page.keyboard.press("Escape")

    def click_outside_menu(self) -> None:
        self.page.click("main")

    def is_menu_open(self) -> bool:
        try:
            return self.locators.solutions_by_initiative.is_visible()
        except Exception:
            return False

    def get_solution_links(self) -> list:
        return self.locators.solution_links.all()
