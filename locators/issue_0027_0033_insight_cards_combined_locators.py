"""Locators for issue_0027-0033: Insight cards combined"""

from playwright.sync_api import Page, Locator


class InsightCardsLocators:
    """Locators for Insight cards."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def insights_section(self) -> Locator:
        """Returns the Insights section."""
        return self.page.get_by_role("heading", name="The intelligence behind the outcomes").locator("..")

    @property
    def download_buttons(self) -> Locator:
        """Returns Download buttons."""
        return self.page.get_by_role("button", name="Download")

    @property
    def read_more_buttons(self) -> Locator:
        """Returns Read More buttons."""
        return self.page.get_by_role("button", name="Read More")
