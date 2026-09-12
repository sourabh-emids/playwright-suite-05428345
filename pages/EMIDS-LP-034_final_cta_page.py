"""Page object for Final CTA section - EMIDS-LP-034, EMIDS-LP-035"""
from playwright.sync_api import Page, expect
from locators.EMIDS-LP-034_final_cta_locators import FinalCTALocators


class FinalCTAPage:
    """Page object for Final CTA section functionality."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = FinalCTALocators(page)

    def goto(self, path: str = "/") -> None:
        self.page.goto(path)

    def verify_section_visible(self) -> None:
        expect(self.locators.section).to_be_visible()

    def verify_timeline_labels(self) -> None:
        expect(self.locators.day_label).to_be_visible()
        expect(self.locators.weeks_label).to_be_visible()
        expect(self.locators.months_label).to_be_visible()

    def click_connect_cta(self) -> None:
        self.locators.connect_cta.click()

    def get_connect_cta_url(self) -> str:
        return self.locators.connect_cta.get_attribute("href")

    def verify_timeline_order(self) -> bool:
        labels = [
            self.locators.day_label.text_content(),
            self.locators.weeks_label.text_content(),
            self.locators.months_label.text_content(),
        ]
        return labels[0] == "1 Day" and labels[1] == "2 Weeks" and labels[2] == "3 Months"
