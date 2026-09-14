"""Page object for the Industries Mega-Menu (issue_0004)."""
from playwright.sync_api import Page, expect
from locators.industries_menu_locators import IndustriesMenuLocators


class IndustriesMenuPage(IndustriesMenuLocators):
    """Page object for Industries mega-menu functionality."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

    def open_industries_menu(self) -> None:
        self.industries_trigger.click()

    def get_industry_count(self) -> int:
        return self.industry_links.count()

    def click_industry(self, industry: str) -> None:
        industry_map = {
            "Payer": self.payer_link,
            "Provider": self.provider_link,
            "HealthTech": self.healthtech_link,
            "Life Sciences": self.life_sciences_link,
            "Consumer": self.consumer_link,
        }
        if industry in industry_map:
            industry_map[industry].click()

    def is_menu_visible(self) -> bool:
        return self.industries_menu.is_visible()
