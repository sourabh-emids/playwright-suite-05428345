"""Locators for Featured solution responsive interaction (issue_0017)."""
from playwright.sync_api import Locator, Page


class FeaturedSolutionsResponsiveLocators:
    """Locators for Featured Solutions responsive elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def solutions_section(self) -> Locator:
        return self.page.get_by_text("A portfolio of named solutions")

    @property
    def carousel_controls(self) -> Locator:
        return self.page.locator("button[aria-label*='previous'], button[aria-label*='next']")
