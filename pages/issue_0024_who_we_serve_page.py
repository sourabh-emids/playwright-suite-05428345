"""Page object for Five audience/industry entries rendering (issue_0024)."""
from playwright.sync_api import Page

from locators.issue_0024_who_we_serve_locators import WhoWeServeLocators


class WhoWeServePage:
    """Page object for Who We Serve section functionality."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = WhoWeServeLocators(page)

    def goto_homepage(self) -> None:
        self.page.goto("/")

    def click_button(self, name: str) -> None:
        if name == "Payer":
            self.locators.payer_button.click()
        elif name == "Provider":
            self.locators.provider_button.click()
        elif name == "HealthTech":
            self.locators.healthtech_button.click()
        elif name == "Life Sciences":
            self.locators.life_sciences_button.click()
        elif name == "Consumer":
            self.locators.consumer_button.click()
