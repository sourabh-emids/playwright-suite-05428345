"""Locators for Reduced motion for partner animation (issue_0019)."""
from playwright.sync_api import Locator, Page


class ReducedMotionPartnersLocators:
    """Locators for reduced motion partner elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def partnerships_section(self) -> Locator:
        return self.page.get_by_text("the world's most powerful technology platforms")
