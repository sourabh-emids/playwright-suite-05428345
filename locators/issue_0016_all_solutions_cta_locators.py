"""Locators for All Solutions CTA functionality (issue_0016)."""
from playwright.sync_api import Locator, Page


class AllSolutionsCTALocators:
    """Locators for All Solutions CTA elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def all_solutions_cta(self) -> Locator:
        return self.page.get_by_role("link", name="All solutions").first
