"""Page object for Responsive and accessible navigation behavior (issue_0008)."""
from playwright.sync_api import Page

from locators.issue_0008_responsive_navigation_locators import ResponsiveNavigationLocators


class ResponsiveNavigationPage:
    """Page object for responsive navigation functionality."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = ResponsiveNavigationLocators(page)

    def goto_homepage(self) -> None:
        self.page.goto("/")

    def open_menu(self) -> None:
        self.locators.solutions_button.click()

    def press_escape(self) -> None:
        self.page.keyboard.press("Escape")

    def tab_through(self, times: int = 5) -> None:
        for _ in range(times):
            self.page.keyboard.press("Tab")

    def set_viewport(self, width: int, height: int) -> None:
        self.page.set_viewport_size({"width": width, "height": height})
