"""Page object for Featured solution responsive interaction (issue_0017)."""
from playwright.sync_api import Page

from locators.issue_0017_featured_solutions_responsive_locators import FeaturedSolutionsResponsiveLocators


class FeaturedSolutionsResponsivePage:
    """Page object for Featured Solutions responsive functionality."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = FeaturedSolutionsResponsiveLocators(page)

    def goto_homepage(self) -> None:
        self.page.goto("/")

    def resize(self, width: int, height: int) -> None:
        self.page.set_viewport_size({"width": width, "height": height})
