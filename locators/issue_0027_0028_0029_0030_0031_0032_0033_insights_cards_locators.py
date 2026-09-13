"""Locators for Medicare Advantage and other eBook/blog card displays (issues 0027-0033)."""
from playwright.sync_api import Locator, Page


class InsightsCardsLocators:
    """Locators for Insights card elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def insights_section(self) -> Locator:
        return self.page.get_by_role("heading", name="The intelligence behind the outcomes")

    @property
    def download_buttons(self) -> Locator:
        return self.page.get_by_role("link", name="Download")

    @property
    def read_more_buttons(self) -> Locator:
        return self.page.get_by_role("link", name="Read More")
