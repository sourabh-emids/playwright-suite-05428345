"""Page object for Industries mega-menu implementation (issue_0004)."""
from playwright.sync_api import Page

from locators.issue_0004_industries_megamenu_locators import IndustriesMegamenuLocators


class IndustriesMegamenuPage:
    """Page object for Industries mega-menu functionality."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = IndustriesMegamenuLocators(page)

    def goto_homepage(self) -> None:
        self.page.goto("/")

    def activate_industries(self) -> None:
        self.locators.industries_button.hover()
        self.page.wait_for_timeout(300)

    def click_payer(self) -> None:
        self.locators.payer_link.click()

    def click_provider(self) -> None:
        self.locators.provider_link.click()

    def click_healthtech(self) -> None:
        self.locators.healthtech_link.click()

    def click_life_sciences(self) -> None:
        self.locators.life_sciences_link.click()

    def click_consumer(self) -> None:
        self.locators.consumer_link.click()

    def is_menu_open(self) -> bool:
        try:
            return self.locators.menu_visible.is_visible()
        except Exception:
            return False
