"""Page object for emids_lp_001: Render global header and brand entry point."""
import re
from typing import List

from playwright.sync_api import Page, expect

from locators.emids_lp_001_header_locators import EmidsLp001HeaderLocators


class EmidsLp001HeaderPage:
    """Page object for header verification."""

    NAV_ITEMS = ["Solutions", "Capabilities", "Industries", "Insights", "Company"]

    def __init__(self, page: Page):
        self.page = page
        self.locators = EmidsLp001HeaderLocators(page)

    def goto_homepage(self) -> None:
        self.page.goto("/")

    def click_logo(self) -> None:
        self.locators.logo.click()

    def get_current_url(self) -> str:
        return self.page.url

    def click_connect_cta(self) -> None:
        self.locators.connect_cta.click()

    def get_nav_items(self) -> List[str]:
        return self.NAV_ITEMS

    def tab_through_navigation(self) -> None:
        self.locators.header.focus()
        self.page.keyboard.press("Tab")

    def is_element_focused(self, locator_name: str) -> bool:
        focused = self.page.evaluate("document.activeElement")
        locators_map = {
            "solutions": self.locators.nav_solutions,
            "capabilities": self.locators.nav_capabilities,
            "industries": self.locators.nav_industries,
            "insights": self.locators.nav_insights,
            "company": self.locators.nav_company,
        }
        locator = locators_map.get(locator_name.lower())
        if locator:
            return self.page.evaluate(
                "(el) => document.activeElement === el",
                locator.element_handle()
            )
        return False

    def get_navigation_urls(self) -> List[str]:
        urls = []
        for item in self.NAV_ITEMS:
            self.locators.nav_solutions.click()
            self.page.wait_for_timeout(300)
        return urls

    def count_connect_cta(self) -> int:
        return self.page.locator('header a[href*="/contact/"], header button:has-text("Connect")').count()

    def get_mobile_menu_items(self) -> List[str]:
        items = []
        self.locators.mobile_menu_button.click()
        self.page.wait_for_timeout(300)
        menu_items = self.page.locator("nav a, nav button")
        count = menu_items.count()
        for i in range(count):
            text = menu_items.nth(i).inner_text()
            if text.strip():
                items.append(text.strip())
        return items
