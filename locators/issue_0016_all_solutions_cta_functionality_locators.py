"""Locators for issue_0016: All Solutions CTA functionality"""

from playwright.sync_api import Page, Locator


class Issue0016AllSolutionsCTALocators:
    """Locators for All Solutions CTA."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def all_solutions_cta(self) -> Locator:
        """Returns the All Solutions CTA link."""
        return self.page.get_by_role("link", name="All solutions")
