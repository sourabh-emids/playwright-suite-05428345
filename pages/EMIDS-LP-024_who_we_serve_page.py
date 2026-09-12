"""Page object for Who We Serve section - EMIDS-LP-024"""
from playwright.sync_api import Page, expect
from locators.EMIDS-LP-024_who_we_serve_locators import WhoWeServeLocators


class WhoWeServePage:
    """Page object for Who We Serve section functionality."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = WhoWeServeLocators(page)

    def goto(self, path: str = "/") -> None:
        self.page.goto(path)

    def verify_section_visible(self) -> None:
        expect(self.locators.section).to_be_visible()

    def verify_all_audiences(self) -> None:
        expect(self.locators.payer_tab).to_be_visible()
        expect(self.locators.provider_tab).to_be_visible()
        expect(self.locators.healthtech_tab).to_be_visible()
        expect(self.locators.life_sciences_tab).to_be_visible()
        expect(self.locators.consumer_tab).to_be_visible()

    def count_audiences(self) -> int:
        return self.locators.payer_tab.count() + self.locators.provider_tab.count()

    def click_explore_cta(self, index: int = 0) -> None:
        self.locators.explore_ctas.nth(index).click()

    def get_audience_urls(self) -> dict[str, str]:
        return {
            "Payer": "/segments/payer/",
            "Provider": "/segments/provider/",
            "HealthTech": "/segments/healthtech/",
            "Life Sciences": "/segments/life-sciences/",
            "Consumer": "/segments/consumer/",
        }
