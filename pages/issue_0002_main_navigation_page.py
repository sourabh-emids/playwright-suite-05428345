"""Page object for desktop main-navigation journeys."""

import re

from playwright.sync_api import expect

from locators.issue_0002_main_navigation_locators import (
    MainNavigationLocators,
)
from pages.issue_0001_website_homepage_page import WebsiteHomepagePage


class MainNavigationPage(WebsiteHomepagePage):
    def open_menu(self, menu_name: str) -> None:
        trigger = self.page.locator(
            MainNavigationLocators.DESKTOP_TRIGGER,
            has_text=menu_name,
        )
        expect(trigger).to_be_visible()
        trigger.click()

    def select_destination(
        self,
        destination_name: str,
        expected_path: str,
    ) -> None:
        destination = self.page.locator(
            MainNavigationLocators.DESKTOP_DESTINATION.format(
                path=expected_path
            )
        )
        active_menu = self.page.locator(
            MainNavigationLocators.ACTIVE_DESKTOP_MENU
        )
        expect(active_menu).to_contain_text(destination_name)
        expect(destination).to_be_visible()
        destination.click()

    def verify_path(self, expected_path: str) -> None:
        path_pattern = re.compile(
            rf".*{re.escape(expected_path)}(?:[?#].*)?$"
        )
        expect(self.page).to_have_url(path_pattern)
