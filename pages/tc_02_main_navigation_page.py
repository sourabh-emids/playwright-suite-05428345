"""Interactions and assertions for the desktop main navigation."""

import re

from playwright.sync_api import Locator, Page, expect

from locators.tc_02_main_navigation_locators import MainNavigationLocators
from pages.base_page import BasePage


class MainNavigationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = MainNavigationLocators()

    @property
    def navigation(self) -> Locator:
        return self.page.get_by_role(
            "navigation", name=self.locators.NAVIGATION_NAME
        )

    def open_homepage(self) -> None:
        self.page.goto("/")
        expect(self.navigation).to_be_visible()

    def select_destination(
        self, menu_name: str, destination_name: str
    ) -> None:
        path = self.locators.DESTINATION_PATHS[destination_name]
        menu_item = self.navigation.get_by_role(
            "link", name=menu_name, exact=True
        )
        expect(menu_item).to_be_visible()
        menu_item.click()
        expect(menu_item).to_have_attribute("aria-expanded", "true")

        destination = menu_item.locator(
            self.locators.MENU_ITEM_ANCESTOR
        ).locator(self.locators.DESTINATION_LINK.format(path=path))
        expect(destination).to_be_visible()
        destination.click()

    def assert_destination(
        self, destination_name: str, heading: str
    ) -> None:
        path = self.locators.DESTINATION_PATHS[destination_name]
        expected_url = re.compile(rf"{re.escape(path)}(?:[?#].*)?$")
        expect(self.page).to_have_url(expected_url)
        expect(
            self.page.get_by_role("heading", name=heading, level=1)
        ).to_be_visible()
