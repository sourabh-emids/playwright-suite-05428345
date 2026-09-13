"""Page object for issue_0005: Insights navigation group"""

from playwright.sync_api import Page, expect

from locators.issue_0005_insights_navigation_group_locators import Issue0005InsightsMenuLocators


class Issue0005InsightsMenuPage:
    """Page object for Insights navigation group."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0005InsightsMenuLocators(page)

    def navigate_to_homepage(self) -> None:
        """Navigate to homepage."""
        self.page.goto("https://www.emids.com")

    def open_insights_menu(self) -> None:
        """Open the Insights menu."""
        self.locators.insights_nav_button.click()

    def resize_to_viewport(self, width: int, height: int) -> None:
        """Resize to specified viewport."""
        self.page.set_viewport_size({"width": width, "height": height})

    def verify_insights_menu_content(self) -> None:
        """Verify Insights menu displays expected content."""
        expect(self.locators.insights_heading).to_be_visible()

    def get_menu_groups(self) -> list[Locator]:
        """Get menu group containers."""
        return self.locators.get_all_insights_links().all()

    def check_empty_groups(self) -> bool:
        """Check if any menu groups are empty."""
        links = self.locators.get_all_insights_links().all()
        for link in links:
            if not link.inner_text():
                return True
        return False
