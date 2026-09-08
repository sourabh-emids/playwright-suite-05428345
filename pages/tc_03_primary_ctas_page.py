import re

from playwright.sync_api import Page, expect

from locators.tc_03_primary_ctas_locators import Tc03PrimaryCtasLocators
from pages.base_page import BasePage


class Tc03PrimaryCtasPage(BasePage):
    ERROR_TEXT = re.compile(
        r"404\s*[-:]?\s*Page Not Found|There has been a critical error|"
        r"This site can.t be reached|ERR_[A-Z_]+",
        re.IGNORECASE,
    )

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = Tc03PrimaryCtasLocators

    def open(self) -> None:
        self.goto("/")
        self._dismiss_cookie_banner()
        expect(self.page.locator(self.locators.MAIN)).to_be_visible()

    def select_primary_call_to_action(self, name: str) -> None:
        call_to_action = self.page.locator(
            self.locators.MAIN
        ).get_by_role("link", name=name, exact=True)
        expect(call_to_action).to_be_visible()
        call_to_action.click()

    def assert_destination_loaded(self, path: str) -> None:
        expected_url = re.compile(
            rf"^https?://[^/]+{re.escape(path)}(?:[?#].*)?$"
        )
        expect(self.page).to_have_url(expected_url)
        expect(self.page.locator(self.locators.MAIN)).to_be_visible()
        expect(self.page.locator(self.locators.BODY)).not_to_contain_text(
            self.ERROR_TEXT
        )

    def _dismiss_cookie_banner(self) -> None:
        allow_all = self.page.get_by_role(
            "button",
            name=self.locators.COOKIE_ALLOW_NAME,
            exact=True,
        )
        if allow_all.count() and allow_all.is_visible():
            allow_all.click()
