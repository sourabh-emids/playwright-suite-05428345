import re

from playwright.sync_api import Page, expect

from locators.issue_0002_navigation_locators import (
    Issue0002NavigationLocators,
)
from pages.base_page import BasePage


class Issue0002NavigationPage(BasePage):
    @property
    def main_navigation(self):
        return self.page.get_by_role(
            "navigation",
            name=Issue0002NavigationLocators.MAIN_NAVIGATION,
        )

    @property
    def visible_mega_menu(self):
        return self.page.locator(
            Issue0002NavigationLocators.VISIBLE_MEGA_MENU
        )

    def open(self) -> None:
        self.page.goto("/")
        self._dismiss_cookie_banner()

    def select_navigation_destination(
        self,
        navigation_item: str,
        destination_name: str,
    ) -> None:
        self.main_navigation.get_by_role(
            "link",
            name=navigation_item,
            exact=True,
        ).click()
        expect(self.visible_mega_menu).to_be_visible()
        expected_path = Issue0002NavigationLocators.DESTINATION_PATHS[
            destination_name
        ]
        destination = self.visible_mega_menu.locator(
            f'a[href$="{expected_path}"]'
        )
        expect(destination).to_be_visible()
        destination.click()

    def assert_destination_opened(self, expected_path: str) -> None:
        expect(self.page).to_have_url(
            re.compile(
                rf".*{re.escape(expected_path)}(?:[?#].*)?$"
            )
        )
        expect(self.page.locator("main")).to_be_visible()

    def _dismiss_cookie_banner(self) -> None:
        allow_button = self.page.get_by_role(
            "button",
            name=Issue0002NavigationLocators.COOKIE_ALLOW_BUTTON,
            exact=True,
        )
        if allow_button.is_visible():
            allow_button.click()
