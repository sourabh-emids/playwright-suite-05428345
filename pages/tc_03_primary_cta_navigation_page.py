"""Page object for TC-03 primary call-to-action navigation."""
from playwright.sync_api import Page, expect

from locators.tc_03_primary_cta_navigation_locators import (
    Tc03PrimaryCtaNavigationLocators,
)
from pages.base_page import BasePage


class Tc03PrimaryCtaNavigationPage(BasePage):
    """Models the inspected primary homepage calls to action."""

    def __init__(self, page: Page):
        super().__init__(page)

    def open_homepage(self) -> None:
        response = self.page.goto("/", wait_until="domcontentloaded")
        assert response is not None and response.ok, "Homepage did not load successfully."
        self.dismiss_cookie_consent_if_present()

    def select_cta(self, cta_name: str) -> None:
        cta = self.page.locator(
            Tc03PrimaryCtaNavigationLocators.CTA_BY_NAME[cta_name]
        )
        expect(cta).to_be_visible()
        cta.click()

    def assert_destination_loaded(self, expected_path: str) -> None:
        self.page.wait_for_url(f"**{expected_path}", wait_until="domcontentloaded")
        expect(self.page.locator("main")).to_be_visible()
        main_text = self.page.locator("main").inner_text().lower()
        assert "page not found" not in main_text
        assert "internal server error" not in main_text
