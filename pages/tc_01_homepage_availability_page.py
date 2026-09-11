"""Page object for TC-01 homepage availability coverage."""
from playwright.sync_api import Page, expect

from locators.tc_01_homepage_availability_locators import (
    Tc01HomepageAvailabilityLocators,
)
from pages.base_page import BasePage


class Tc01HomepageAvailabilityPage(BasePage):
    """Models the public Emids homepage health checks."""

    def __init__(self, page: Page):
        super().__init__(page)

    def open(self) -> None:
        """Open the homepage and ensure the server returned a success response."""
        response = self.page.goto("/", wait_until="domcontentloaded")
        assert response is not None, "Homepage navigation did not return a response."
        assert response.ok, f"Homepage returned HTTP {response.status}."
        self.dismiss_cookie_consent_if_present()

    def assert_loaded_without_obvious_error(self) -> None:
        """Assert meaningful homepage content exists and error-page text does not."""
        expect(
            self.page.locator(Tc01HomepageAvailabilityLocators.MAIN_CONTENT)
        ).to_be_visible()
        expect(
            self.page.locator(Tc01HomepageAvailabilityLocators.HERO_HEADING)
        ).to_be_visible()
        visible_text = self.page.locator(
            Tc01HomepageAvailabilityLocators.MAIN_CONTENT
        ).inner_text().lower()
        prohibited_messages = (
            "page not found",
            "internal server error",
            "something went wrong",
            "access denied",
        )
        assert not any(message in visible_text for message in prohibited_messages), (
            "Homepage contains an obvious error message."
        )
