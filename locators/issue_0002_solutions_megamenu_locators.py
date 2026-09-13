"""Locators for Solutions mega-menu implementation (issue_0002)."""
from playwright.sync_api import Locator, Page


class SolutionsMegamenuLocators:
    """Locators for Solutions mega-menu elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def solutions_button(self) -> Locator:
        return self.page.get_by_role("button", name="Solutions")

    @property
    def solutions_menu(self) -> Locator:
        return self.page.locator('[aria-label="Solutions menu"], .solutions-menu, nav button:has-text("Solutions") + *')

    @property
    def solution_links(self) -> Locator:
        return self.page.locator(".solutions-menu a, [aria-label='Solutions menu'] a")

    @property
    def solutions_by_initiative(self) -> Locator:
        return self.page.get_by_text("Solutions by Initiative")

    @property
    def browse_by_industry(self) -> Locator:
        return self.page.get_by_text("Browse By Industry")

    @property
    def the_portfolio(self) -> Locator:
        return self.page.get_by_text("The Portfolio")
