"""Locators for issue_0005: Insights navigation group"""

from playwright.sync_api import Page, Locator


class Issue0005InsightsMenuLocators:
    """Locators for the Insights navigation group."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def insights_nav_button(self) -> Locator:
        """Returns the Insights navigation button."""
        return self.page.get_by_role("button", name="Insights")

    @property
    def insights_heading(self) -> Locator:
        """Returns the Insights and Resources heading."""
        return self.page.get_by_text("Insights and Resources")

    @property
    def news_heading(self) -> Locator:
        """Returns the News & Events heading."""
        return self.page.get_by_text("News & Events")

    def get_all_insights_links(self) -> Locator:
        """Returns all links in the Insights menu."""
        return self.page.locator("button:has-text('Insights') ~ a")
