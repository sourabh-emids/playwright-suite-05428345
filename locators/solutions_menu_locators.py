"""Locators for the Solutions Mega-Menu (issue_0002)."""
from playwright.sync_api import Locator, Page


class SolutionsMenuLocators:
    """Locators for the Solutions mega-menu component."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def solutions_trigger(self) -> Locator:
        return self.page.get_by_role("button", name="Solutions")

    @property
    def solutions_menu(self) -> Locator:
        return self.page.locator('[aria-label*="Solutions"], .solutions-menu, nav:has(button:has-text("Solutions")) + *')

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
        return self.page.locator('a:has-text("Modernization"), a:has-text("Interoperability"), a:has-text("Cloud Transformation"), a:has-text("Agentic AI"), a:has-text("Global Capability Center")')

    @property
    def modernization_link(self) -> Locator:
        return self.page.get_by_role("link", name="Modernization")

    @property
    def interoperability_link(self) -> Locator:
        return self.page.get_by_role("link", name="Interoperability")

    @property
    def cloud_transformation_link(self) -> Locator:
        return self.page.get_by_role("link", name="Cloud Transformation")

    @property
    def agentic_ai_link(self) -> Locator:
        return self.page.get_by_role("link", name="Agentic AI")

    @property
    def global_capability_center_link(self) -> Locator:
        return self.page.get_by_role("link", name="Global Capability Center")

    @property
    def menu_close_trigger(self) -> Locator:
        return self.page.get_by_role("button", name="Solutions")
