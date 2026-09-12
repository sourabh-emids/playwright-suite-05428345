"""Page object for Insights menu - EMIDS-LP-005"""
from playwright.sync_api import Page, expect
from locators.EMIDS-LP-005_insights_menu_locators import InsightsMenuLocators


class InsightsMenuPage:
    """Page object for Insights menu functionality."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = InsightsMenuLocators(page)

    def goto(self, path: str = "/") -> None:
        self.page.goto(path)

    def open_insights_menu(self) -> None:
        self.locators.insights_trigger.click()

    def verify_menu_groups(self) -> None:
        expect(self.locators.insights_resources_group).to_be_visible()
        expect(self.locators.news_events_group).to_be_visible()

    def get_insights_links(self) -> list[str]:
        links = []
        for i in range(self.locators.insights_links.count()):
            link = self.locators.insights_links.nth(i)
            href = link.get_attribute("href")
            if href:
                links.append(href)
        return links
