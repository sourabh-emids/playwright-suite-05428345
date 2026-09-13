"""Page object for Insights navigation group implementation (issue_0005)."""
from playwright.sync_api import Page

from locators.issue_0005_insights_navigation_locators import InsightsNavigationLocators


class InsightsNavigationPage:
    """Page object for Insights navigation functionality."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = InsightsNavigationLocators(page)

    def goto_homepage(self) -> None:
        self.page.goto("/")

    def activate_insights(self) -> None:
        self.locators.insights_button.hover()
        self.page.wait_for_timeout(300)

    def is_menu_open(self) -> bool:
        try:
            return self.locators.menu_visible.is_visible()
        except Exception:
            return False
