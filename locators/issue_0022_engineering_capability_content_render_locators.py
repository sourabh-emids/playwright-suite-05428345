"""Locators for issue_0022: Engineering capability content render"""

from playwright.sync_api import Page, Locator


class Issue0022EngineeringCapabilityLocators:
    """Locators for Engineering capability content."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def engineering_content(self) -> Locator:
        """Returns the Engineering content."""
        return self.page.get_by_text("Engineering")
