"""Locators for issue_0019: Reduced motion for partner animation"""

from playwright.sync_api import Page, Locator


class Issue0019ReducedMotionLocators:
    """Locators for reduced motion settings."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def partnerships_section(self) -> Locator:
        """Returns the Partnerships section."""
        return self.page.locator("section").filter(has_text="technology platforms").first
