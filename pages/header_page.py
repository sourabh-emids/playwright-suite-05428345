"""Page object for the Global Header Navigation (issue_0001)."""
from playwright.sync_api import expect, Page
from locators.header_locators import HeaderLocators


class HeaderPage(HeaderLocators):
    """Page object for header functionality."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

    def goto_homepage(self) -> None:
        self.page.goto("/")

    def click_logo(self) -> None:
        self.logo.click()

    def click_connect_cta(self) -> None:
        self.connect_cta.click()

    def click_nav_item(self, name: str) -> None:
        button = self.page.get_by_role("button", name=name)
        button.click()

    def open_solutions_menu(self) -> None:
        self.solutions_nav.click()

    def open_capabilities_menu(self) -> None:
        self.capabilities_nav.click()

    def open_industries_menu(self) -> None:
        self.industries_nav.click()

    def open_insights_menu(self) -> None:
        self.insights_nav.click()

    def open_company_menu(self) -> None:
        self.company_nav.click()

    def tab_through_nav(self) -> None:
        self.page.keyboard.press("Tab")

    def hover_nav_item(self, name: str) -> None:
        button = self.page.get_by_role("button", name=name)
        button.hover()

    def is_header_visible(self) -> bool:
        return self.header.is_visible()

    def count_connect_ctas(self) -> int:
        return self.page.get_by_role("link", name="Connect").count()

    def get_current_url(self) -> str:
        return self.page.url
