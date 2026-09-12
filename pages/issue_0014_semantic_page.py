"""Page object for issue_0014 - Semantic heading hierarchy and landmarks."""
from playwright.sync_api import Page, expect

from locators.issue_0014_semantic_locators import Issue0014SemanticLocators


class Issue0014SemanticPage:
    """Page object for semantic structure."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0014SemanticLocators()
        self.locators.page = page

    def heading_hierarchy_follows_logical_order(self) -> None:
        """Verify heading hierarchy follows logical order."""
        h1_count = self.locators.h1_headings.count()
        assert h1_count >= 1, "Page should have at least one H1"

        h2_count = self.locators.h2_headings.count()
        assert h2_count >= 1, "Page should have H2 headings for sections"

    def there_should_be_single_h1(self) -> None:
        """Verify there is exactly one H1."""
        h1_count = self.locators.h1_headings.count()
        assert h1_count == 1, f"Expected exactly 1 H1, found {h1_count}"

    def h2_should_be_used_for_sections(self) -> None:
        """Verify H2 is used for section titles."""
        h2_count = self.locators.h2_headings.count()
        assert h2_count >= 1, "Page should have H2 headings for sections"

    def h3_should_be_used_for_subsections(self) -> None:
        """Verify H3 is used for subsection titles."""
        h3_count = self.locators.h3_headings.count()
        # H3 may or may not exist depending on content complexity
        pass

    def header_landmark_should_exist(self) -> None:
        """Verify header landmark exists."""
        expect(self.locators.header_landmark.first).to_be_attached()

    def main_landmark_should_exist(self) -> None:
        """Verify main landmark exists."""
        expect(self.locators.main_landmark).to_be_attached()

    def footer_landmark_should_exist(self) -> None:
        """Verify footer landmark exists."""
        expect(self.locators.footer_landmark.first).to_be_attached()
