"""Page object for TC-02 main navigation destinations."""

import re

from playwright.sync_api import Locator, expect

from locators.tc_02_main_navigation_locators import (
    MEGA_MENU,
    MENU_LINK,
    NAVIGATION_TARGETS,
    NAVIGATION_TRIGGER,
)
from pages.base_page import BasePage


class MainNavigationPage(BasePage):
    """Controls the desktop mega navigation and verifies its destinations."""

    def load(self) -> None:
        self.page.set_viewport_size({"width": 1280, "height": 900})
        self.goto("/")
        self.dismiss_cookie_banner()

    def target_for(self, menu_name: str) -> dict[str, str]:
        return NAVIGATION_TARGETS[menu_name]

    def open_menu(self, menu_name: str) -> Locator:
        target = self.target_for(menu_name)
        trigger = self.page.locator(NAVIGATION_TRIGGER.format(menu=target["menu"]))
        trigger.click()
        expect(trigger).to_have_attribute("aria-expanded", "true")
        return self.page.locator(MEGA_MENU.format(menu=target["menu"]))

    def open_expected_destination(self, menu_name: str) -> None:
        target = self.target_for(menu_name)
        menu = self.open_menu(menu_name)
        link = menu.locator(MENU_LINK.format(path=target["path"])).first
        expect(link).to_be_visible()
        link.click()
        expect(self.page).to_have_url(re.compile(re.escape(target["path"]) + r"$"))
