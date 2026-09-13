"""Locators for Insights section and six content cards (issue_0026)."""
from playwright.sync_api import Locator, Page


class InsightsSectionLocators:
    """Locators for Insights section elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def insights_section(self) -> Locator:
        return self.page.get_by_role("heading", name="The intelligence behind the outcomes")

    @property
    def insight_cards(self) -> Locator:
        return self.page.locator(".insight-card, .resource-card, [data-insight]")

    @property
    def download_buttons(self) -> Locator:
        return self.page.get_by_role("link", name="Download")

    @property
    def read_more_buttons(self) -> Locator:
        return self.page.get_by_role("link", name="Read More")
