"""Page object for Partnerships section - EMIDS-LP-018, EMIDS-LP-019"""
from playwright.sync_api import Page, expect
from locators.EMIDS-LP-018_partnerships_locators import PartnershipsLocators


class PartnershipsPage:
    """Page object for Partnerships section functionality."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = PartnershipsLocators(page)

    def goto(self, path: str = "/") -> None:
        self.page.goto(path)

    def verify_section_visible(self) -> None:
        expect(self.locators.section).to_be_visible()

    def count_partner_logos(self) -> int:
        return self.locators.partner_logos.count()

    def verify_logo_alt_text(self) -> list[str]:
        alt_texts = []
        for i in range(self.locators.partner_logos.count()):
            alt = self.locators.partner_logos.nth(i).get_attribute("alt")
            if alt:
                alt_texts.append(alt)
        return alt_texts

    def verify_partner_logo_loaded(self) -> None:
        first_logo = self.locators.partner_logos.first
        expect(first_logo).to_be_visible()
