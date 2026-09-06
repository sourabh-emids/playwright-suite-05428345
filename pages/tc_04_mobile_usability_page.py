"""Responsive usability checks for the agreed mobile viewport."""

import re

from playwright.sync_api import Page, expect

from locators.tc_04_mobile_usability_locators import (
    MobileUsabilityLocators,
)
from pages.base_page import BasePage


class MobileUsabilityPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = MobileUsabilityLocators()

    def open_in_mobile_view(self) -> None:
        self.page.set_viewport_size(self.locators.VIEWPORT)
        self.page.goto("/")

    def assert_primary_content_is_usable(self) -> None:
        logo = self.page.get_by_alt_text(self.locators.LOGO_ALT_TEXT).first
        hero = self.page.get_by_role(
            "heading", name=self.locators.HERO_HEADING, level=1
        )
        primary_cta = self.page.get_by_role(
            "link", name=self.locators.PRIMARY_CTA, exact=True
        )
        menu_toggle = self.page.get_by_role(
            "button", name=self.locators.MENU_TOGGLE
        )

        for element in (logo, hero, primary_cta, menu_toggle):
            expect(element).to_be_visible()

        if not logo.evaluate("image => image.complete && image.naturalWidth > 0"):
            raise AssertionError("The mobile header logo is broken")

        has_horizontal_overflow = self.page.evaluate(
            "document.documentElement.scrollWidth > window.innerWidth + 1"
        )
        if has_horizontal_overflow:
            raise AssertionError("The mobile page has horizontal overflow")

    def navigate_with_mobile_menu(self) -> None:
        menu_toggle = self.page.get_by_role(
            "button", name=self.locators.MENU_TOGGLE
        )
        menu_toggle.click()

        solutions = self.page.get_by_role(
            "button", name=self.locators.SOLUTIONS_MENU, exact=True
        )
        expect(solutions).to_be_visible()
        solutions.click()

        solutions_link = solutions.locator(
            self.locators.MENU_SECTION
        ).locator(self.locators.SOLUTIONS_LINK)
        expect(solutions_link).to_be_visible()
        solutions_link.click()

    def assert_mobile_navigation_destination(self) -> None:
        expect(self.page).to_have_url(
            re.compile(r"/solutions/(?:[?#].*)?$")
        )
        expect(
            self.page.get_by_role(
                "heading", name=self.locators.SOLUTIONS_HEADING, level=1
            )
        ).to_be_visible()
