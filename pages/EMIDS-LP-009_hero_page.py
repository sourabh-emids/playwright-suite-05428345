"""Page object for Hero section - EMIDS-LP-009, EMIDS-LP-010, EMIDS-LP-011"""
from playwright.sync_api import Page, expect
from locators.EMIDS-LP-009_hero_locators import HeroLocators


class HeroPage:
    """Page object for Hero section functionality."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = HeroLocators(page)

    def goto(self, path: str = "/") -> None:
        self.page.goto(path)

    def verify_h1_content(self) -> None:
        expect(self.locators.h1_heading).to_contain_text("In Healthcare, Only Outcomes Matter")

    def get_h1_text(self) -> str:
        return self.locators.h1_heading.text_content()

    def count_h1_elements(self) -> int:
        return self.page.locator("h1").count()

    def click_hero_cta(self) -> None:
        self.locators.hero_cta.click()

    def get_hero_cta_url(self) -> str:
        return self.locators.hero_cta.get_attribute("href")

    def get_hero_cta_target(self) -> str:
        return self.locators.hero_cta.get_attribute("target")

    def verify_hero_cta_https(self) -> bool:
        url = self.get_hero_cta_url()
        return url and url.startswith("https://")

    def verify_canonical_fcde(self) -> bool:
        url = self.get_hero_cta_url()
        return url and "/forward-deployed-context-engineering/" in url
