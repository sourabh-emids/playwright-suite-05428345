"""Locators for issue_0015: Render six featured solutions"""

from playwright.sync_api import Page, Locator


class Issue0015FeaturedSolutionsLocators:
    """Locators for Featured Solutions section."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def featured_solutions_section(self) -> Locator:
        """Returns the Featured Solutions section."""
        return self.page.get_by_text("A portfolio of named solutions").locator("..")

    @property
    def all_solutions_link(self) -> Locator:
        """Returns the All solutions link."""
        return self.page.get_by_role("link", name="All solutions")

    @property
    def solution_items(self) -> Locator:
        """Returns solution item containers."""
        return self.page.locator("a[href*='/solutions/']")
