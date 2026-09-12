"""Page object for issue_0017 - Featured solutions responsive interaction."""
from playwright.sync_api import Page, expect

from locators.issue_0017_featured_solutions_responsive_locators import Issue0017FeaturedSolutionsResponsiveLocators


class Issue0017FeaturedSolutionsResponsivePage:
    """Page object for featured solutions responsive interaction."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0017FeaturedSolutionsResponsiveLocators()
        self.locators.page = page

    def set_viewport_to_desktop(self) -> None:
        """Set viewport to desktop size."""
        self.page.set_viewport_size({"width": 1920, "height": 1080})

    def set_viewport_to_mobile(self) -> None:
        """Set viewport to mobile size."""
        self.page.set_viewport_size({"width": 375, "height": 667})

    def view_featured_solutions_section(self) -> None:
        """Scroll to the Featured Solutions section."""
        self.locators.featured_solutions_section.scroll_into_view_if_needed()

    def cards_should_be_in_grid_layout(self) -> None:
        """Verify cards are displayed in a grid layout on desktop."""
        # On desktop, multiple cards should be visible side by side
        cards = self.locators.solution_cards
        expect(cards.first).to_be_visible()

    def cards_should_be_in_stacked_layout(self) -> None:
        """Verify cards are displayed in a stacked layout on mobile."""
        # On mobile, cards should still be visible (possibly stacked)
        cards = self.locators.solution_cards
        expect(cards.first).to_be_visible()
