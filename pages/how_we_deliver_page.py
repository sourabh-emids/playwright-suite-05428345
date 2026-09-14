"""Page object for the How We Deliver module (issues 0012, 0013)."""
from playwright.sync_api import Page, expect
from locators.how_we_deliver_locators import HowWeDeliverLocators


class HowWeDeliverPage(HowWeDeliverLocators):
    """Page object for How We Deliver functionality."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

    def click_see_model_cta(self) -> None:
        self.cta.click()

    def get_cta_href(self) -> str:
        return self.cta.get_attribute("href")

    def is_section_visible(self) -> bool:
        return self.section.is_visible()
