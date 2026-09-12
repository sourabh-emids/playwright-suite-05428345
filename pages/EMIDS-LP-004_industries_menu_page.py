"""Page object for Industries mega-menu - EMIDS-LP-004"""
from playwright.sync_api import Page, expect
from locators.EMIDS-LP-004_industries_menu_locators import IndustriesMenuLocators


class IndustriesMenuPage:
    """Page object for Industries mega-menu functionality."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = IndustriesMenuLocators(page)

    def goto(self, path: str = "/") -> None:
        self.page.goto(path)

    def open_industries_menu(self) -> None:
        self.locators.industries_trigger.click()

    def verify_all_audiences(self) -> None:
        expect(self.locators.payer_link).to_be_visible()
        expect(self.locators.provider_link).to_be_visible()
        expect(self.locators.healthtech_link).to_be_visible()
        expect(self.locators.life_sciences_link).to_be_visible()
        expect(self.locators.consumer_link).to_be_visible()

    def get_audience_urls(self) -> dict[str, str]:
        return {
            "Payer": self.locators.payer_link.get_attribute("href"),
            "Provider": self.locators.provider_link.get_attribute("href"),
            "HealthTech": self.locators.healthtech_link.get_attribute("href"),
            "Life Sciences": self.locators.life_sciences_link.get_attribute("href"),
            "Consumer": self.locators.consumer_link.get_attribute("href"),
        }
