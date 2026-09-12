"""Page object for How We Deliver section - EMIDS-LP-012, EMIDS-LP-013"""
from playwright.sync_api import Page, expect
from locators.EMIDS-LP-012_how_we_deliver_locators import HowWeDeliverLocators


class HowWeDeliverPage:
    """Page object for How We Deliver section functionality."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = HowWeDeliverLocators(page)

    def goto(self, path: str = "/") -> None:
        self.page.goto(path)

    def verify_section_visible(self) -> None:
        expect(self.locators.section).to_be_visible()

    def verify_section_heading(self) -> None:
        expect(self.locators.section_heading).to_be_visible()

    def click_see_model_cta(self) -> None:
        self.locators.see_the_model_cta.click()

    def get_see_model_cta_url(self) -> str:
        return self.locators.see_the_model_cta.get_attribute("href")

    def verify_see_model_cta_routes_fdce(self) -> bool:
        url = self.get_see_model_cta_url()
        return url and "/forward-deployed-context-engineering/" in url

    def focus_and_activate_see_model(self) -> None:
        self.locators.see_the_model_cta.focus()
        self.page.keyboard.press("Enter")

    def verify_heading_hierarchy(self) -> None:
        h2 = self.page.locator("h2").first
        h3 = self.page.locator("h3").first
        expect(h2).to_be_visible()
        expect(h3).to_be_visible()
