"""Locators for issue_0017 - Featured solutions responsive interaction."""
from playwright.sync_api import Locator


class Issue0017FeaturedSolutionsResponsiveLocators:
    """Locators for featured solutions responsive behavior."""

    @property
    def featured_solutions_section(self) -> Locator:
        """Return the Featured Solutions section."""
        return self.page.locator("text=A portfolio of named solutions").locator("..")

    @property
    def solution_cards(self) -> Locator:
        """Return the solution cards."""
        return self.featured_solutions_section.locator("article, [class*='card']")
