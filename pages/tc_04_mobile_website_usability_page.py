"""Page object for TC-04 mobile homepage usability."""
from playwright.sync_api import Locator, Page, expect

from locators.tc_04_mobile_website_usability_locators import (
    Tc04MobileWebsiteUsabilityLocators,
)
from pages.base_page import BasePage


class Tc04MobileWebsiteUsabilityPage(BasePage):
    """Models essential controls in the inspected 390px mobile layout."""

    MOBILE_WIDTH = 390
    MOBILE_HEIGHT = 844

    def __init__(self, page: Page):
        super().__init__(page)

    def open_in_mobile_view(self) -> None:
        self.page.set_viewport_size(
            {"width": self.MOBILE_WIDTH, "height": self.MOBILE_HEIGHT}
        )
        response = self.page.goto("/", wait_until="domcontentloaded")
        assert response is not None and response.ok, "Homepage did not load successfully."
        self.dismiss_cookie_consent_if_present()

    def assert_initial_content_is_usable(self) -> None:
        self._assert_in_viewport(
            self.page.locator(Tc04MobileWebsiteUsabilityLocators.LOGO)
        )
        self._assert_in_viewport(
            self.page.locator(Tc04MobileWebsiteUsabilityLocators.MENU_TOGGLE)
        )
        self._assert_in_viewport(
            self.page.locator(Tc04MobileWebsiteUsabilityLocators.HERO_HEADING)
        )
        hero_image = self.page.locator(
            Tc04MobileWebsiteUsabilityLocators.HERO_IMAGE
        ).first
        self._assert_in_viewport(hero_image)
        assert hero_image.evaluate(
            "image => image.complete && image.naturalWidth > 0"
        ), "The visible mobile image did not load."
        self._assert_in_viewport(
            self.page.locator(Tc04MobileWebsiteUsabilityLocators.HERO_CTA)
        )
        horizontal_scroll_width = self.page.evaluate("document.documentElement.scrollWidth")
        assert horizontal_scroll_width <= self.MOBILE_WIDTH, (
            "The mobile page requires horizontal scrolling."
        )

    def open_mobile_menu(self) -> None:
        toggle = self.page.locator(Tc04MobileWebsiteUsabilityLocators.MENU_TOGGLE)
        expect(toggle).to_be_visible()
        toggle.click()

    def assert_mobile_menu_controls_are_usable(self) -> None:
        self._assert_in_viewport(
            self.page.locator(Tc04MobileWebsiteUsabilityLocators.MOBILE_MENU_LINK)
        )
        self._assert_in_viewport(
            self.page.locator(Tc04MobileWebsiteUsabilityLocators.MOBILE_CONNECT_CTA)
        )

    def _assert_in_viewport(self, locator: Locator) -> None:
        locator.scroll_into_view_if_needed()
        expect(locator).to_be_visible()
        box = locator.bounding_box()
        assert box is not None, "Visible control did not have layout bounds."
        assert box["x"] >= 0 and box["x"] + box["width"] <= self.MOBILE_WIDTH, (
            "Control extends outside the mobile viewport."
        )
        assert box["width"] > 0 and box["height"] > 0, "Control has no usable size."
