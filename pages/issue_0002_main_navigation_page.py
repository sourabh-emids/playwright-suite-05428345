"""Page object for the desktop main navigation."""

import re

from playwright.sync_api import Page, expect

from locators.issue_0002_main_navigation_locators import (
    MainNavigationLocators,
)
from pages.issue_0001_homepage_availability_page import (
    HomepageAvailabilityPage,
)


class MainNavigationPage(HomepageAvailabilityPage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.navigation_locators = MainNavigationLocators

    def select_menu_destination(
        self,
        menu: str,
        destination: str,
    ) -> None:
        navigation = self.page.get_by_role(
            "navigation",
            name=self.navigation_locators.NAVIGATION,
        )
        navigation.get_by_role(
            "link",
            name=menu,
            exact=True,
        ).click()

        active_menu = self.page.locator(
            self.navigation_locators.ACTIVE_MENU
        )
        expect(active_menu).to_be_visible()
        if menu == self.navigation_locators.INDUSTRIES:
            industry = active_menu.locator(
                self.navigation_locators.INDUSTRY_ITEM
            ).filter(has_text=destination).first
            expect(industry).to_be_visible()
            destination_link = industry.get_by_role(
                "link",
                name=self.navigation_locators.INDUSTRY_DESTINATION_ACTION,
            ).first
        else:
            exact_destination = active_menu.get_by_role(
                "link",
                name=destination,
                exact=True,
            )
            if exact_destination.count():
                destination_link = exact_destination.first
            else:
                destination_link = active_menu.get_by_role("link").filter(
                    has_text=destination
                ).first

        expect(destination_link).to_be_enabled()
        destination_link.click()

    def select_connect(self) -> None:
        self.page.get_by_role("banner").get_by_role(
            "link",
            name=self.navigation_locators.CONNECT,
            exact=True,
        ).click()

    def assert_destination(self, path: str, heading: str) -> None:
        url_pattern = re.compile(
            rf".*{re.escape(path)}(?:[?#].*)?$"
        )
        expect(self.page).to_have_url(url_pattern)
        expect(
            self.page.get_by_role(
                "heading",
                name=heading,
                exact=True,
            )
        ).to_be_visible()
