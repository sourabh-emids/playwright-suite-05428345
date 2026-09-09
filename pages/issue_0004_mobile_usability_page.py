"""Page object for mobile homepage usability."""

import re

from playwright.sync_api import Page, expect

from locators.issue_0004_mobile_usability_locators import (
    MobileUsabilityLocators,
)
from pages.issue_0001_homepage_availability_page import (
    HomepageAvailabilityPage,
)


class MobileUsabilityPage(HomepageAvailabilityPage):
    MOBILE_WIDTH = 390
    MOBILE_HEIGHT = 844

    def __init__(self, page: Page):
        super().__init__(page)
        self.mobile_locators = MobileUsabilityLocators

    def open_in_mobile_view(self) -> None:
        self.page.set_viewport_size(
            {
                "width": self.MOBILE_WIDTH,
                "height": self.MOBILE_HEIGHT,
            }
        )
        self.open()

    def assert_primary_content_is_usable(self) -> None:
        banner = self.page.get_by_role("banner")
        logo = banner.get_by_role(
            "img",
            name=self.mobile_locators.LOGO,
        )
        heading = self.page.get_by_role(
            "heading",
            name=self.mobile_locators.HERO_HEADING,
            level=1,
        )
        call_to_action = self.page.get_by_role("main").get_by_role(
            "link",
            name=self.mobile_locators.HERO_CALL_TO_ACTION,
            exact=True,
        )

        for element in (logo, heading, call_to_action):
            expect(element).to_be_visible()
            expect(element).to_be_in_viewport()
        expect(call_to_action).to_be_enabled()
        assert self.page.evaluate(
            "document.documentElement.scrollWidth <= window.innerWidth"
        ), "The mobile page has unintended horizontal overflow."

    def open_contact_from_mobile_navigation(self) -> None:
        self.page.get_by_role(
            "button",
            name=self.mobile_locators.MENU_TOGGLE,
        ).click()
        mobile_menu = self.page.locator(
            self.mobile_locators.MOBILE_MENU
        )
        expect(mobile_menu).to_be_visible()

        company = mobile_menu.get_by_role(
            "button",
            name=self.mobile_locators.COMPANY,
            exact=True,
        )
        expect(company).to_be_visible()
        expect(company).to_be_enabled()
        company.click()

        contact = mobile_menu.get_by_role("link").filter(
            has_text=self.mobile_locators.CONTACT_US
        )
        expect(contact).to_be_visible()
        expect(contact).to_be_enabled()
        contact.click()

    def assert_contact_page_opened(self) -> None:
        expect(self.page).to_have_url(
            re.compile(r".*/contact/(?:[?#].*)?$")
        )
        expect(
            self.page.get_by_role(
                "heading",
                name=self.mobile_locators.CONTACT_HEADING,
                exact=True,
            )
        ).to_be_visible()
