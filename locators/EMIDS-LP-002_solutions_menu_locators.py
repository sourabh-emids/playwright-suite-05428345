"""Locators for Solutions mega-menu - EMIDS-LP-002"""
from playwright.sync_api import Page, Locator


class SolutionsMenuLocators:
    """Locators for Solutions mega-menu elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def solutions_nav(self) -> Locator:
        return self.page.get_by_role("navigation", name="Main Navigation").get_by_role("link", name="Solutions")

    @property
    def solutions_trigger(self) -> Locator:
        return self.page.get_by_role("button", name="Solutions").first

    @property
    def mega_menu(self) -> Locator:
        return self.page.locator("header").locator('div:has(button:has-text("Solutions"))').first

    @property
    def solutions_by_initiative(self) -> Locator:
        return self.page.get_by_text("Solutions by Initiative")

    @property
    def browse_by_industry(self) -> Locator:
        return self.page.get_by_text("Browse By Industry")

    @property
    def the_portfolio(self) -> Locator:
        return self.page.get_by_text("The Portfolio")

    @property
    def solution_links(self) -> Locator:
        return self.page.locator('a[href*="/solutions/"]')
