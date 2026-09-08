import re

from playwright.sync_api import Page, expect

from locators.tc_01_homepage_locators import Tc01HomepageLocators
from pages.base_page import BasePage


class Tc01HomepagePage(BasePage):
    ERROR_TEXT = re.compile(
        r"404\s*[-:]?\s*Page Not Found|There has been a critical error|"
        r"This site can.t be reached|ERR_[A-Z_]+",
        re.IGNORECASE,
    )

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = Tc01HomepageLocators

    def open(self) -> None:
        self.goto("/")

    def assert_primary_content(self) -> None:
        expect(self.page).to_have_title(re.compile(r"Emids", re.IGNORECASE))
        expect(
            self.page.get_by_role(
                "heading",
                name=self.locators.HOME_HEADING,
                exact=True,
            )
        ).to_be_visible()
        expect(
            self.page.get_by_role("banner").get_by_role(
                "img",
                name=self.locators.LOGO_NAME,
            )
        ).to_be_visible()
        expect(
            self.page.locator(self.locators.MAIN).get_by_role(
                "link",
                name=self.locators.PRIMARY_CTA_NAME,
                exact=True,
            )
        ).to_be_visible()

    def assert_no_visible_load_failure(self) -> None:
        expect(self.page.locator(self.locators.MAIN)).to_be_visible()
        expect(self.page.locator(self.locators.BODY)).not_to_contain_text(
            self.ERROR_TEXT
        )
