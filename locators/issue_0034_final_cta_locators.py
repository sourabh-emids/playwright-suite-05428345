"""Locators for Final conversion banner rendering (issue_0034)."""
from playwright.sync_api import Locator, Page


class FinalCTALocators:
    """Locators for Final CTA section elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def final_cta_section(self) -> Locator:
        return self.page.get_by_role("heading", name="From workshop to agent to scale deployment")

    @property
    def connect_cta(self) -> Locator:
        return self.page.get_by_role("link", name="Connect").last

    @property
    def footer(self) -> Locator:
        return self.page.locator("footer")
