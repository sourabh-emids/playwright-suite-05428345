"""Page object for TC-02 desktop mega-navigation routing."""
from playwright.sync_api import Page, expect

from locators.tc_02_main_navigation_routing_locators import (
    Tc02MainNavigationRoutingLocators,
)
from pages.base_page import BasePage


class Tc02MainNavigationRoutingPage(BasePage):
    """Models navigation triggers and their first intended destinations."""

    def __init__(self, page: Page):
        super().__init__(page)

    def open_homepage(self) -> None:
        response = self.page.goto("/", wait_until="domcontentloaded")
        assert response is not None and response.ok, (
            "Homepage did not load successfully."
        )
        self.dismiss_cookie_consent_if_present()
        expect(
            self.page.locator(Tc02MainNavigationRoutingLocators.MAIN_NAVIGATION)
        ).to_be_visible()

    def select_menu_destination(self, menu_name: str) -> None:
        """Open a top-level mega-menu and follow its inspected destination link."""
        trigger = self.page.locator(
            Tc02MainNavigationRoutingLocators.TRIGGER_BY_MENU[menu_name]
        )
        expect(trigger).to_be_visible()
        trigger.click()

        destination = self.page.locator(
            Tc02MainNavigationRoutingLocators.DESTINATION_BY_MENU[menu_name]
        )
        expect(destination).to_be_visible()
        destination.click()

    def assert_destination_loaded(self, expected_path: str) -> None:
        self.page.wait_for_url(f"**{expected_path}", wait_until="domcontentloaded")
        expect(self.page.locator("main")).to_be_visible()
        main_text = self.page.locator("main").inner_text().lower()
        assert "page not found" not in main_text
        assert "internal server error" not in main_text
