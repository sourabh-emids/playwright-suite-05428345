"""Page object for TC-01 homepage availability."""

from playwright.sync_api import expect

from locators.tc_01_homepage_loads_successfully_locators import (
    HERO_HEADING,
    HOME_PATH,
    MAIN_NAVIGATION,
)
from pages.base_page import BasePage


class HomepageAvailabilityPage(BasePage):
    """Interactions and assertions for the public homepage."""

    def load(self) -> None:
        self.page.set_viewport_size({"width": 1280, "height": 900})
        self.goto(HOME_PATH)
        self.dismiss_cookie_banner()

    def assert_loaded(self) -> None:
        expect(self.page).to_have_title(
            "Emids - Digital Engineering, Core Platforms, and AI Solutions"
        )
        expect(self.page.locator(HERO_HEADING)).to_be_visible()
        expect(self.page.locator(MAIN_NAVIGATION)).to_be_visible()

    def visible_error_text(self) -> str:
        return self.page.locator("body").inner_text().lower()
