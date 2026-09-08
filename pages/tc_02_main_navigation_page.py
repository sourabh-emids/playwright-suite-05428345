import re

from playwright.sync_api import Page, expect

from locators.tc_02_main_navigation_locators import (
    Tc02MainNavigationLocators,
)
from pages.base_page import BasePage


class Tc02MainNavigationPage(BasePage):
    ERROR_TEXT = re.compile(
        r"404\s*[-:]?\s*Page Not Found|There has been a critical error|"
        r"This site can.t be reached|ERR_[A-Z_]+",
        re.IGNORECASE,
    )

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = Tc02MainNavigationLocators

    def open(self) -> None:
        self.goto("/")
        self._dismiss_cookie_banner()
        expect(
            self.page.get_by_role(
                "navigation",
                name=self.locators.NAVIGATION_NAME,
            )
        ).to_be_visible()

    def select_destination(self, menu: str, path: str) -> None:
        navigation = self.page.get_by_role(
            "navigation",
            name=self.locators.NAVIGATION_NAME,
        )
        trigger = navigation.get_by_role(
            "link",
            name=menu,
            exact=True,
        )
        trigger.click()
        expect(trigger).to_have_attribute("aria-expanded", "true")

        selector = self.locators.ACTIVE_MENU_DESTINATION.format(path=path)
        destination = self.page.locator(selector)
        expect(destination).to_be_visible()
        destination.click()

    def assert_destination_loaded(self, path: str) -> None:
        expected_url = re.compile(
            rf"^https?://[^/]+{re.escape(path)}(?:[?#].*)?$"
        )
        expect(self.page).to_have_url(expected_url)
        expect(self.page.locator(self.locators.MAIN)).to_be_visible()
        expect(self.page.locator(self.locators.BODY)).not_to_contain_text(
            self.ERROR_TEXT
        )

    def _dismiss_cookie_banner(self) -> None:
        allow_all = self.page.get_by_role(
            "button",
            name=self.locators.COOKIE_ALLOW_NAME,
            exact=True,
        )
        if allow_all.count() and allow_all.is_visible():
            allow_all.click()
