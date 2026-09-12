"""Page object for issue_0005 - Insights navigation group accessibility."""
from playwright.sync_api import Page, expect

from locators.issue_0005_insights_menu_locators import Issue0005InsightsMenuLocators


class Issue0005InsightsMenuPage:
    """Page object for Insights navigation group accessibility."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0005InsightsMenuLocators()
        self.locators.page = page

    def click_insights_navigation(self) -> None:
        """Click the Insights navigation item."""
        self.locators.insights_nav_button.click()

    def mega_menu_should_appear(self) -> None:
        """Verify mega-menu appears."""
        expect(self.locators.insights_and_resources_header).to_be_visible()

    def menu_should_display_header(self, header: str) -> None:
        """Verify a header is displayed in the menu."""
        if header == "Insights and Resources":
            expect(self.locators.insights_and_resources_header).to_be_visible()
        elif header == "News & Events":
            expect(self.locators.news_and_events_header).to_be_visible()

    def insights_hub_link_should_be_present(self) -> None:
        """Verify Insights Hub link is present."""
        expect(self.locators.insights_hub_link).to_be_visible()

    def case_studies_link_should_be_present(self) -> None:
        """Verify Case Studies link is present."""
        expect(self.locators.case_studies_link).to_be_visible()

    def ebooks_guides_link_should_be_present(self) -> None:
        """Verify eBooks & Guides link is present."""
        expect(self.locators.ebooks_guides_link).to_be_visible()

    def webinars_link_should_be_present(self) -> None:
        """Verify Webinars link is present."""
        expect(self.locators.webinars_link).to_be_visible()
