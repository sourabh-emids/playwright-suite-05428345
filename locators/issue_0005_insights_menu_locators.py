"""Locators for issue_0005 - Insights navigation group accessibility."""
from playwright.sync_api import Locator


class Issue0005InsightsMenuLocators:
    """Locators for Insights navigation group."""

    @property
    def insights_nav_button(self) -> Locator:
        """Return the Insights navigation button."""
        return self.page.locator('button:has-text("Insights")')

    @property
    def insights_and_resources_header(self) -> Locator:
        """Return the 'Insights and Resources' header."""
        return self.page.locator("text=Insights and Resources")

    @property
    def news_and_events_header(self) -> Locator:
        """Return the 'News & Events' header."""
        return self.page.locator("text=News & Events")

    @property
    def insights_hub_link(self) -> Locator:
        """Return the Insights Hub link."""
        return self.page.get_by_role("link", name="Insights Hub")

    @property
    def case_studies_link(self) -> Locator:
        """Return the Case Studies link."""
        return self.page.get_by_role("link", name="Case Studies")

    @property
    def ebooks_guides_link(self) -> Locator:
        """Return the eBooks & Guides link."""
        return self.page.get_by_role("link", name="eBooks & Guides")

    @property
    def webinars_link(self) -> Locator:
        """Return the Webinars link."""
        return self.page.get_by_role("link", name="Webinars")
