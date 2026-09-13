"""Page object for emids_lp_005: Implement Insights navigation group."""
from playwright.sync_api import Page, expect
from locators.emids_lp_005_insights_nav_locators import InsightsNavLocators


class InsightsNavPage:
    """Insights navigation page object."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = InsightsNavLocators(page)

    @property
    def url(self) -> str:
        """Homepage URL."""
        return "/"

    def navigate(self) -> None:
        """Navigate to the homepage."""
        self.page.goto("/")

    def open_insights_menu(self) -> None:
        """Open the Insights menu."""
        self.locators.insights_nav.click()
        self.page.wait_for_selector('[role="menu"]', state="visible", timeout=5000)

    def close_insights_menu(self) -> None:
        """Close the Insights menu."""
        self.page.keyboard.press("Escape")

    def are_groups_visible(self) -> bool:
        """Check if group labels are visible."""
        return (
            self.locators.insights_and_resources.is_visible()
            and self.locators.news_and_events.is_visible()
        )

    def get_child_links(self) -> list[Locator]:
        """Get all child links."""
        return self.locators.get_all_links()

    def has_empty_groups(self) -> bool:
        """Check for empty menu groups."""
        for link in self.locators.get_all_links():
            if not link.is_visible():
                return True
        return False

    def click_insights_link(self, link_name: str) -> None:
        """Click an insights link by name."""
        link_lower = link_name.lower()
        if "insights hub" in link_lower:
            self.locators.insights_hub_link.click()
        elif "case studies" in link_lower:
            self.locators.case_studies_link.click()
        elif "ebook" in link_lower or "guide" in link_lower:
            self.locators.ebooks_guides_link.click()
        elif "webinar" in link_lower:
            self.locators.webinars_link.click()
        elif "summit" in link_lower:
            self.locators.healthcare_summit_link.click()
        elif "event" in link_lower:
            self.locators.events_link.click()
        elif "news" in link_lower:
            self.locators.news_link.click()
