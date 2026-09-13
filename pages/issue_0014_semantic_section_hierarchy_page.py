"""Page object for issue_0014: Semantic section hierarchy"""

from playwright.sync_api import Page, expect

from locators.issue_0014_semantic_section_hierarchy_locators import Issue0014SemanticHierarchyLocators


class Issue0014SemanticHierarchyPage:
    """Page object for semantic section hierarchy."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0014SemanticHierarchyLocators(page)

    def navigate_to_homepage(self) -> None:
        """Navigate to homepage."""
        self.page.goto("https://www.emids.com")

    def count_h1_elements(self) -> int:
        """Count H1 elements."""
        return self.page.get_by_role("heading", level=1).count()

    def get_heading_levels(self) -> list:
        """Get all heading levels."""
        headings = self.page.locator("h1, h2, h3, h4, h5, h6").all()
        return [int(h.evaluate("el => el.tagName.slice(1)")) for h in headings]

    def verify_landmarks_exist(self) -> None:
        """Verify semantic landmarks exist."""
        expect(self.locators.main_landmark).to_be_visible()
        expect(self.locators.header_landmark).to_be_visible()
        expect(self.locators.footer_landmark).to_be_visible()

    def check_heading_progression(self) -> bool:
        """Check if heading progression is logical."""
        levels = self.get_heading_levels()
        # Check for skipped levels (e.g., H1 to H4 without H2/H3)
        for i in range(len(levels) - 1):
            if levels[i + 1] - levels[i] > 1:
                return False
        return True
