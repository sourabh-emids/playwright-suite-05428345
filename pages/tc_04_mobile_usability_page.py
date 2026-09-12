"""Page object for TC-04 mobile usability."""

from playwright.sync_api import expect

from locators.tc_04_mobile_usability_locators import (
    MOBILE_HERO,
    MOBILE_HERO_CTA,
    MOBILE_LOGO,
    MOBILE_MENU_TOGGLE,
    MOBILE_MENU_TRIGGER,
)
from pages.base_page import BasePage


class MobileUsabilityPage(BasePage):
    """Verifies core content and controls at a mobile viewport."""

    def set_mobile_viewport(self) -> None:
        self.page.set_viewport_size({"width": 390, "height": 844})

    def load(self) -> None:
        self.goto("/")
        self.dismiss_cookie_banner()

    def assert_core_content_visible(self) -> None:
        expect(self.page.locator(MOBILE_LOGO)).to_be_visible()
        expect(self.page.locator(MOBILE_HERO)).to_be_visible()
        expect(self.page.locator(MOBILE_HERO_CTA)).to_be_visible()
        expect(self.page.locator(MOBILE_MENU_TOGGLE)).to_be_visible()

    def open_mobile_menu(self) -> None:
        self.page.locator(MOBILE_MENU_TOGGLE).click()
        expect(self.page.locator(MOBILE_MENU_TRIGGER)).to_be_visible()

    def assert_menu_control_usable(self) -> None:
        menu_button = self.page.locator(MOBILE_MENU_TRIGGER)
        expect(menu_button).to_be_enabled()
        menu_button.click()
        expect(menu_button).to_be_visible()
