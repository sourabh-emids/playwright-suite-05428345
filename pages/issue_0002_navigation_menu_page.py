"""Page object for issue_0002: Main navigation menu items work correctly."""
from playwright.sync_api import Page, expect

from locators.issue_0002_navigation_menu_locators import NavigationMenuLocators


class NavigationMenuPage:
    """Page object for the main navigation menu."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = NavigationMenuLocators(page)

    def navigate_to_homepage(self) -> None:
        self.page.goto("/")

    def click_solutions_menu(self) -> None:
        self.locators.solutions_link.click()
        expect(self.page).to_have_url("**/solutions/**")

    def click_capabilities_menu(self) -> None:
        self.locators.capabilities_link.click()
        expect(self.page).to_have_url("**/capabilities/**")

    def click_industries_menu(self) -> None:
        self.locators.industries_link.click()
        expect(self.page).to_have_url("**/segments/**")

    def click_insights_menu(self) -> None:
        self.locators.insights_link.click()
        expect(self.page).to_have_url("**/insights/**")

    def click_company_menu(self) -> None:
        self.locators.company_link.click()
        expect(self.page).to_have_url("**/about-us/**")

    def click_connect_menu(self) -> None:
        self.locators.connect_link.click()
        expect(self.page).to_have_url("**/contact/**")
