"""Locators for emids_lp_005: Implement Insights navigation group."""
from playwright.sync_api import Locator, Page


class InsightsNavLocators:
    """Insights navigation locators."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def insights_nav(self) -> Locator:
        """Insights navigation item in header."""
        return self.page.get_by_role("link", name="Insights")

    @property
    def insights_button(self) -> Locator:
        """Insights button for mega-menu trigger."""
        return self.page.get_by_role("button", name="Insights")

    @property
    def insights_menu(self) -> Locator:
        """Insights menu container."""
        return self.page.locator('[aria-label="Insights menu"], [role="menu"]').first

    @property
    def insights_and_resources(self) -> Locator:
        """Insights and Resources group label."""
        return self.page.get_by_text("Insights and Resources")

    @property
    def news_and_events(self) -> Locator:
        """News and Events group label."""
        return self.page.get_by_text("News & Events")

    @property
    def insights_hub_link(self) -> Locator:
        """Insights Hub link."""
        return self.page.get_by_role("link", name="Insights Hub")

    @property
    def case_studies_link(self) -> Locator:
        """Case Studies link."""
        return self.page.get_by_role("link", name="Case Studies")

    @property
    def ebooks_guides_link(self) -> Locator:
        """eBooks & Guides link."""
        return self.page.get_by_role("link", name="eBooks & Guides")

    @property
    def webinars_link(self) -> Locator:
        """Webinars link."""
        return self.page.get_by_role("link", name="Webinars")

    @property
    def healthcare_summit_link(self) -> Locator:
        """Healthcare Summit link."""
        return self.page.get_by_role("link", name="Healthcare Summit")

    @property
    def events_link(self) -> Locator:
        """Events link."""
        return self.page.get_by_role("link", name="Events")

    @property
    def news_link(self) -> Locator:
        """News link."""
        return self.page.get_by_role("link", name="News")

    def get_insights_links(self) -> list[Locator]:
        """Get all Insights and Resources links."""
        return [
            self.insights_hub_link,
            self.case_studies_link,
            self.ebooks_guides_link,
            self.webinars_link,
        ]

    def get_news_events_links(self) -> list[Locator]:
        """Get all News & Events links."""
        return [
            self.healthcare_summit_link,
            self.events_link,
            self.news_link,
        ]

    def get_all_links(self) -> list[Locator]:
        """Get all links."""
        return self.get_insights_links() + self.get_news_events_links()
