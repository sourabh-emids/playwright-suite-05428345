"""Page object for Company navigation group implementation (issue_0006)."""
from playwright.sync_api import Page

from locators.issue_0006_company_navigation_locators import CompanyNavigationLocators


class CompanyNavigationPage:
    """Page object for Company navigation functionality."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = CompanyNavigationLocators(page)

    def goto_homepage(self) -> None:
        self.page.goto("/")

    def activate_company(self) -> None:
        self.locators.company_button.hover()
        self.page.wait_for_timeout(300)

    def click_company(self) -> None:
        self.locators.company_button.click()

    def is_menu_open(self) -> bool:
        try:
            return self.locators.menu_visible.is_visible()
        except Exception:
            return False
