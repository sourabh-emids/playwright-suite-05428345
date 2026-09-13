"""Locators for issue_0017: Featured solutions responsive interaction"""

from playwright.sync_api import Page, Locator


class Issue0017FeaturedSolutionsResponsiveLocators:
    """Locators for Featured Solutions responsive interaction."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def solution_items(self) -> Locator:
        """Returns solution items."""
        return self.page.locator("a[href*='/solutions/']")

    @property
    def previous_button(self) -> Locator:
        """Returns carousel previous button if present."""
        return self.page.get_by_role("button", name="Previous").first

    @property
    def next_button(self) -> Locator:
        """Returns carousel next button if present."""
        return self.page.get_by_role("button", name="Next").first
