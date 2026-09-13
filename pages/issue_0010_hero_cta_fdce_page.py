"""Page object for Hero CTA routes to FDCE experience (issue_0010)."""
from playwright.sync_api import Page

from locators.issue_0010_hero_cta_fdce_locators import HeroCTAFDCELocators


class HeroCTAFDCEPage:
    """Page object for Hero CTA FDCE functionality."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = HeroCTAFDCELocators(page)

    def goto_homepage(self) -> None:
        self.page.goto("/")

    def click_hero_cta(self) -> None:
        self.locators.hero_cta.click()

    def get_cta_href(self) -> str:
        return self.locators.hero_cta.get_attribute("href")
