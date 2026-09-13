"""Locators for emids_lp_002: Implement Solutions mega-menu."""
from playwright.sync_api import Locator, Page


class EmidsLp002SolutionsLocators:
    """Locators for Solutions mega-menu verification."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def solutions_button(self) -> Locator:
        return self.page.get_by_role("button", name="Solutions")

    @property
    def mega_menu(self) -> Locator:
        return self.page.locator('[role="menu"], .mega-menu, [aria-expanded="true"]').filter(has=self.page.locator("text=Solutions"))

    @property
    def solutions_links(self) -> Locator:
        return self.mega_menu.locator("a, button").or_(self.page.locator('[role="menuitem"], [role="menuitemradio"]'))

    @property
    def solutions_by_initiative_group(self) -> Locator:
        return self.page.locator("text=Solutions by Initiative").or_(self.page.locator('[aria-label*="Solutions by Initiative"]'))

    @property
    def browse_by_industry_group(self) -> Locator:
        return self.page.locator("text=Browse By Industry")

    @property
    def portfolio_group(self) -> Locator:
        return self.page.locator("text=The Portfolio")
