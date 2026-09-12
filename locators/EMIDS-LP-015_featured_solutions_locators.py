"""Locators for Featured Solutions section - EMIDS-LP-015, EMIDS-LP-016, EMIDS-LP-017"""
from playwright.sync_api import Page, Locator


class FeaturedSolutionsLocators:
    """Locators for Featured Solutions section elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def section(self) -> Locator:
        return self.page.get_by_text("A portfolio of named solutions")

    @property
    def solution_cards(self) -> Locator:
        return self.page.locator('a[href*="/solutions/"]')

    @property
    def solution_01(self) -> Locator:
        return self.page.get_by_role("heading", name="Modernization as a Service")

    @property
    def solution_02(self) -> Locator:
        return self.page.get_by_role("heading", name="Interoperability")

    @property
    def solution_03(self) -> Locator:
        return self.page.get_by_role("heading", name="Cloud Migration")

    @property
    def solution_04(self) -> Locator:
        return self.page.get_by_role("heading", name="Global Capability Center")

    @property
    def solution_05(self) -> Locator:
        return self.page.get_by_role("heading", name="Epic Implementation")

    @property
    def solution_06(self) -> Locator:
        return self.page.get_by_role("heading", name="Agentic AI")

    @property
    def all_solutions_cta(self) -> Locator:
        return self.page.get_by_role("link", name="All solutions")
