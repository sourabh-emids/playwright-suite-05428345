"""Locators for Insights section - EMIDS-LP-026, EMIDS-LP-027, EMIDS-LP-028, EMIDS-LP-029, EMIDS-LP-030, EMIDS-LP-031, EMIDS-LP-032, EMIDS-LP-033"""
from playwright.sync_api import Page, Locator


class InsightsLocators:
    """Locators for Insights section elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def section(self) -> Locator:
        return self.page.get_by_text("The intelligence behind the outcomes")

    @property
    def insight_cards(self) -> Locator:
        return self.section.locator('a[href*="/insights/"]')

    @property
    def medicare_ebook_card(self) -> Locator:
        return self.page.get_by_role("link", name="Managing the Margin Reset in Medicare Advantage")

    @property
    def cms0057_card(self) -> Locator:
        return self.page.get_by_role("link", name="CMS-0057: The Interoperability Imperative")

    @property
    def life_sciences_ebook_card(self) -> Locator:
        return self.page.get_by_role("link", name="Unlocking Trusted Digital Transformation in Life Sciences")

    @property
    def ai_roi_ebook_card(self) -> Locator:
        return self.page.get_by_role("link", name="Closing the AI ROI Gap in Healthcare")

    @property
    def finops_card(self) -> Locator:
        return self.page.locator('a:has-text("FinOps")')

    @property
    def payer_data_blog_card(self) -> Locator:
        return self.page.get_by_role("link", name="Payers: Is Your Data Ready for AI?")

    @property
    def download_buttons(self) -> Locator:
        return self.page.get_by_role("button", name="Download")

    @property
    def read_more_buttons(self) -> Locator:
        return self.page.get_by_role("button", name="Read More")
