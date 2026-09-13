"""Locators for issue_0021: AI capability content render"""

from playwright.sync_api import Page, Locator


class Issue0021AICapabilityLocators:
    """Locators for AI capability content."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def ai_capability_section(self) -> Locator:
        """Returns the AI capability section."""
        return self.page.get_by_text("AI").locator("..")
