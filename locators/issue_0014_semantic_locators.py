"""Locators for issue_0014 - Semantic heading hierarchy and landmarks."""
from playwright.sync_api import Locator


class Issue0014SemanticLocators:
    """Locators for semantic structure."""

    @property
    def h1_headings(self) -> Locator:
        """Return all H1 headings."""
        return self.page.get_by_role("heading", level=1)

    @property
    def h2_headings(self) -> Locator:
        """Return all H2 headings."""
        return self.page.get_by_role("heading", level=2)

    @property
    def h3_headings(self) -> Locator:
        """Return all H3 headings."""
        return self.page.get_by_role("heading", level=3)

    @property
    def header_landmark(self) -> Locator:
        """Return the header landmark."""
        return self.page.locator("header, banner")

    @property
    def main_landmark(self) -> Locator:
        """Return the main landmark."""
        return self.page.locator("main")

    @property
    def footer_landmark(self) -> Locator:
        """Return the footer landmark."""
        return self.page.locator("footer, contentinfo")
