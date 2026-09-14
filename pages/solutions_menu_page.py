"""Page object for the Solutions Mega-Menu (issue_0002)."""
from playwright.sync_api import Page, expect
from locators.solutions_menu_locators import SolutionsMenuLocators


class SolutionsMenuPage(SolutionsMenuLocators):
    """Page object for Solutions mega-menu functionality."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

    def open_solutions_menu(self) -> None:
        self.solutions_trigger.click()

    def close_solutions_menu(self) -> None:
        self.solutions_trigger.click()

    def press_escape(self) -> None:
        self.page.keyboard.press("Escape")

    def get_solution_link_count(self) -> int:
        return self.solution_links.count()

    def click_solution(self, name: str) -> None:
        link_map = {
            "Modernization": self.modernization_link,
            "Interoperability": self.interoperability_link,
            "Cloud Transformation": self.cloud_transformation_link,
            "Agentic AI": self.agentic_ai_link,
            "Global Capability Center": self.global_capability_center_link,
        }
        if name in link_map:
            link_map[name].click()

    def tab_through_menu(self) -> None:
        self.page.keyboard.press("Tab")

    def is_menu_visible(self) -> bool:
        return self.solutions_menu.is_visible()

    def focus_trigger(self) -> None:
        self.solutions_trigger.focus()
