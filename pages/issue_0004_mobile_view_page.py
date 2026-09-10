"""Page object for the supported mobile-sized homepage."""

import re

from playwright.sync_api import expect

from locators.issue_0001_website_homepage_locators import (
    WebsiteHomepageLocators,
)
from locators.issue_0004_mobile_view_locators import MobileViewLocators
from pages.issue_0001_website_homepage_page import WebsiteHomepagePage


class MobileViewPage(WebsiteHomepagePage):
    VIEWPORT = {"width": 390, "height": 844}

    def use_supported_viewport(self) -> None:
        self.page.set_viewport_size(self.VIEWPORT)

    def verify_mobile_content(self) -> None:
        expect(
            self.page.get_by_role(
                "heading",
                name=WebsiteHomepageLocators.HERO_HEADING_NAME,
                exact=True,
            )
        ).to_be_visible()
        expect(
            self.page.locator(MobileViewLocators.HEADER_LOGO)
        ).to_be_visible()
        expect(
            self.page.locator(MobileViewLocators.HERO_ACTION)
        ).to_be_visible()
        expect(
            self.page.locator(MobileViewLocators.MOBILE_MENU_TOGGLE)
        ).to_be_visible()

    def open_solutions_menu(self) -> None:
        self.page.locator(MobileViewLocators.MOBILE_MENU_TOGGLE).click()
        solutions = self.page.locator(
            MobileViewLocators.MOBILE_MENU_TRIGGER,
            has_text="Solutions",
        )
        expect(solutions).to_be_visible()
        solutions.click()

    def verify_modernization_accessible(self) -> None:
        expect(
            self.page.locator(MobileViewLocators.MODERNIZATION_LINK)
        ).to_be_visible()

    def select_modernization(self) -> None:
        self.page.locator(MobileViewLocators.MODERNIZATION_LINK).click()

    def verify_modernization_page(self) -> None:
        expect(self.page).to_have_url(
            re.compile(r".*/solutions/modernization-as-a-service/?$")
        )
