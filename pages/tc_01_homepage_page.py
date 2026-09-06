"""Homepage availability checks."""

from playwright.sync_api import Page, expect

from locators.tc_01_homepage_locators import HomepageLocators
from pages.base_page import BasePage


class HomepagePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = HomepageLocators()

    def open(self) -> None:
        response = self.page.goto("/")
        if response is None or not response.ok:
            status = response.status if response else "no response"
            raise AssertionError(f"Homepage request failed: {status}")

    def assert_loaded_without_visible_errors(self) -> None:
        expect(
            self.page.get_by_role(
                "heading", name=self.locators.HERO_HEADING, level=1
            )
        ).to_be_visible()
        expect(
            self.page.get_by_role(
                "navigation", name=self.locators.MAIN_NAVIGATION
            )
        ).to_be_visible()
        expect(
            self.page.locator(self.locators.MAIN_CONTENT)
        ).to_be_visible()

        logo = self.page.get_by_alt_text(self.locators.LOGO_ALT_TEXT).first
        expect(logo).to_be_visible()
        if not logo.evaluate("image => image.complete && image.naturalWidth > 0"):
            raise AssertionError("The visible Emids logo is broken")

        main = self.page.locator(self.locators.MAIN_CONTENT)
        for error_text in self.locators.VISIBLE_ERROR_TEXTS:
            expect(main.get_by_text(error_text, exact=False)).to_have_count(0)
