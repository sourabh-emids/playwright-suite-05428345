"""Page object for Global header visibility and Emids brand link (issue_0001)."""
from playwright.sync_api import Page, expect

from locators.issue_0001_header_locators import HeaderLocators


class HeaderPage:
    """Page object for header navigation functionality."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = HeaderLocators(page)

    def goto_homepage(self) -> None:
        self.page.goto("/")

    def goto_any_page(self, path: str) -> None:
        self.page.goto(path)

    def click_logo(self) -> None:
        self.locators.logo.click()

    def hover_over_nav_item(self, button_name: str) -> None:
        if button_name == "Solutions":
            self.locators.solutions_button.hover()
        elif button_name == "Capabilities":
            self.locators.capabilities_button.hover()
        elif button_name == "Industries":
            self.locators.industries_button.hover()
        elif button_name == "Insights":
            self.locators.insights_button.hover()
        elif button_name == "Company":
            self.locators.company_button.hover()

    def click_nav_item(self, button_name: str) -> None:
        if button_name == "Solutions":
            self.locators.solutions_button.click()
        elif button_name == "Capabilities":
            self.locators.capabilities_button.click()
        elif button_name == "Industries":
            self.locators.industries_button.click()
        elif button_name == "Insights":
            self.locators.insights_button.click()
        elif button_name == "Company":
            self.locators.company_button.click()
        elif button_name == "Connect":
            self.locators.connect_cta.click()

    def navigate_with_keyboard(self) -> None:
        self.locators.header.focus()
        self.page.keyboard.press("Tab")

    def is_header_visible(self) -> bool:
        return self.locators.header.is_visible()

    def count_connect_ctas(self) -> int:
        return self.locators.header.get_by_role("link", name="Connect").count()

    def set_viewport_width(self, width: int) -> None:
        self.page.set_viewport_size({"width": width, "height": 768})
