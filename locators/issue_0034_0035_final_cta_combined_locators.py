"""Locators for issue_0034-0035: Final CTA combined"""

from playwright.sync_api import Page, Locator


class FinalCTALocators:
    """Locators for Final CTA section."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def final_cta_section(self) -> Locator:
        """Returns the final CTA section."""
        return self.page.get_by_role("heading", name="From workshop to agent to scale deployment").locator("..")

    @property
    def connect_cta(self) -> Locator:
        """Returns the Connect CTA."""
        return self.page.get_by_role("link", name="Connect").last

    @property
    def timing_labels(self) -> Locator:
        """Returns timing labels."""
        return self.page.get_by_text("1 Day · 2 Weeks · 3 Months")
