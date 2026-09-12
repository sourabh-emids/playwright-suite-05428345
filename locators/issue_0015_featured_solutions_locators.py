"""Locators for issue_0015 - Six featured solutions rendering and numbering."""
from playwright.sync_api import Locator


class Issue0015FeaturedSolutionsLocators:
    """Locators for Featured Solutions section."""

    @property
    def featured_solutions_section(self) -> Locator:
        """Return the Featured Solutions section."""
        return self.page.locator("text=A portfolio of named solutions")

    @property
    def solution_cards(self) -> Locator:
        """Return the solution cards."""
        return self.featured_solutions_section.locator("..").locator("article, [class*='card'], [class*='solution']")
