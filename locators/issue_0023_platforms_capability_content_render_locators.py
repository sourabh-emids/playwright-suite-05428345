"""Locators for issue_0023: Platforms capability content render"""

from playwright.sync_api import Page, Locator


class Issue0023PlatformsCapabilityLocators:
    """Locators for Platforms capability content."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def platforms_content(self) -> Locator:
        """Returns the Platforms content."""
        return self.page.get_by_text("Platforms")
