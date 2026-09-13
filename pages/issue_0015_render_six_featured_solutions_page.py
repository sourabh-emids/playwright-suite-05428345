"""Page object for issue_0015: Render six featured solutions"""

from playwright.sync_api import Page, expect

from locators.issue_0015_render_six_featured_solutions_locators import Issue0015FeaturedSolutionsLocators


class Issue0015FeaturedSolutionsPage:
    """Page object for Featured Solutions section."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0015FeaturedSolutionsLocators(page)

    def navigate_to_homepage(self) -> None:
        """Navigate to homepage."""
        self.page.goto("https://www.emids.com")

    def count_solution_items(self) -> int:
        """Count the solution items."""
        return self.locators.solution_items.count()

    def verify_six_items(self) -> None:
        """Verify exactly six items are present."""
        count = self.count_solution_items()
        expect(count).to_be(6)

    def check_for_specific_titles(self) -> dict:
        """Check for specific solution titles."""
        content = self.page.content()
        return {
            "Modernization as a Service": "Modernization as a Service" in content,
            "Interoperability": "Interoperability" in content,
            "Cloud Migration": "Cloud Migration" in content,
            "Global Capability Center": "Global Capability Center" in content,
            "Epic Implementation": "Epic Implementation" in content,
            "Agentic AI": "Agentic AI" in content,
        }

    def verify_all_solutions_link(self) -> None:
        """Verify All Solutions link is present."""
        expect(self.locators.all_solutions_link).to_be_visible()
