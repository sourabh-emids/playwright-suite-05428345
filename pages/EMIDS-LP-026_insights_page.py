"""Page object for Insights section - EMIDS-LP-026, EMIDS-LP-027, EMIDS-LP-028, EMIDS-LP-029, EMIDS-LP-030, EMIDS-LP-031, EMIDS-LP-032, EMIDS-LP-033"""
from playwright.sync_api import Page, expect
from locators.EMIDS-LP-026_insights_locators import InsightsLocators


class InsightsPage:
    """Page object for Insights section functionality."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = InsightsLocators(page)

    def goto(self, path: str = "/") -> None:
        self.page.goto(path)

    def verify_section_visible(self) -> None:
        expect(self.locators.section).to_be_visible()

    def count_insight_cards(self) -> int:
        return self.locators.insight_cards.count()

    def verify_medicare_ebook(self) -> None:
        expect(self.locators.medicare_ebook_card).to_be_visible()

    def get_medicare_ebook_url(self) -> str:
        return self.locators.medicare_ebook_card.get_attribute("href")

    def verify_cms0057_card(self) -> None:
        expect(self.locators.cms0057_card).to_be_visible()

    def verify_life_sciences_ebook(self) -> None:
        expect(self.locators.life_sciences_ebook_card).to_be_visible()

    def get_life_sciences_ebook_url(self) -> str:
        return self.locators.life_sciences_ebook_card.get_attribute("href")

    def verify_ai_roi_ebook(self) -> None:
        expect(self.locators.ai_roi_ebook_card).to_be_visible()

    def verify_payer_data_blog(self) -> None:
        expect(self.locators.payer_data_blog_card).to_be_visible()

    def count_download_buttons(self) -> int:
        return self.locators.download_buttons.count()

    def count_read_more_buttons(self) -> int:
        return self.locators.read_more_buttons.count()
